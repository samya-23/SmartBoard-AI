import tkinter as tk
from game import Game
from gui_view import BoardView

class GameApp:
    def __init__(self, root):
        self.root = root
        root.title("Deep Sea Diver - GUI")

        self.container = tk.Frame(root)
        self.container.pack()

        self.game = Game(board_size=20, player_names=["A", "B", "BOT", "D", "E", "F"])
        self.view = BoardView(self.container, 20)
        self.view.grid(row=0, column=0, rowspan=3, padx=10)

        self.info_frame = tk.Frame(self.container)
        self.info_frame.grid(row=0, column=1, sticky="nw")

        self.status = tk.Label(self.info_frame, text="", font=("Arial", 10))
        self.status.pack(pady=5)

        self.survivor_label = tk.Label(self.info_frame, text="", font=("Arial", 10))
        self.survivor_label.pack(pady=5)

        self.bot_decision_label = tk.Label(
            self.info_frame, text="", font=("Courier", 9),
            justify="left", wraplength=250, fg="blue"
        )
        self.bot_decision_label.pack(pady=10)

        self.move_button = tk.Button(
            self.info_frame, text="Next Move", command=self.next_move, font=("Arial", 12)
        )
        self.move_button.pack(pady=10)

        self.restart_button = tk.Button(
            self.info_frame, text="Restart Game", command=self.restart_game, font=("Arial", 10)
        )
        self.restart_button.pack(pady=5)

        self.elim_frame = tk.Frame(self.container)
        self.elim_frame.grid(row=1, column=1, sticky="nw")

        self.elim_label = tk.Label(
            self.elim_frame, text="❌ Eliminated Players:", font=("Arial", 10, "bold")
        )
        self.elim_label.pack(anchor="w")

        self.elim_list = tk.Label(
            self.elim_frame, text="", font=("Arial", 10), fg="gray", justify="left"
        )
        self.elim_list.pack(anchor="w")

        self.update_ui()

    def update_ui(self, jump_to=None):
        survivors = self.game.get_survivors()
        eliminated = self.game.get_eliminated_players()

        self.view.update_board(self.game, flash_index=jump_to, animate=True)

        if self.game.is_game_over():
            if self.game.winner:
                self.status.config(text=f"🏆 {self.game.winner.name} wins!")
            else:
                self.status.config(text="🤝 Game Over — No more valid moves.")
            self.move_button.config(state="disabled")
        else:
            if self.game.current and self.game.current.tile is not None:
                self.status.config(text=f"{self.game.current.name}'s turn")
            else:
                self.status.config(text="Waiting for valid player...")

        self.survivor_label.config(
            text=f"Survivors: {len(survivors)} / {self.game.total_players}"
        )

        if self.game.last_bot_decision:
            self.bot_decision_label.config(text=self.game.last_bot_decision)
        else:
            self.bot_decision_label.config(text="")

        elim_names = [
            f"{p.name} (out at Tile {self.game.eliminated.get(p.name).position})"
            for p in eliminated
        ]
        self.elim_list.config(text="\n".join(elim_names) if elim_names else "None")

    def next_move(self):
        jump_to = self.game.move()

        # Skip eliminated players before UI update
        checked = 0
        while self.game.current and self.game.current.tile is None and checked < self.game.total_players:
            self.game.current = self.game.current.next
            checked += 1

        self.update_ui(jump_to)

    def restart_game(self):
        self.game.reset()
        self.move_button.config(state="normal")
        self.update_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()