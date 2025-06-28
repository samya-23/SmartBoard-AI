import tkinter as tk
from game import Game
from gui_view import BoardView

class GameApp:
    def __init__(self, root):
        self.root = root
        root.title("Deep Sea Diver - GUI")

        self.game = Game(board_size=20, player_names=["A", "B", "C", "D", "E", "F"])
        self.view = BoardView(root, 20)
        self.view.pack(pady=10)

        self.move_button = tk.Button(root, text="Next Move", command=self.next_move, font=("Arial", 12))
        self.move_button.pack()

        self.status = tk.Label(root, text="", font=("Arial", 10))
        self.status.pack()

        self.view.update_board(self.game)

    def next_move(self):
        self.game.move()
        self.view.update_board(self.game)
        self.status.config(text=f"{self.game.current.name}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
