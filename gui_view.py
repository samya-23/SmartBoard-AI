import tkinter as tk

class BoardView(tk.Canvas):
    def __init__(self, root, board_size):
        super().__init__(root, width=40 * board_size + 20, height=100, bg="white")
        self.tiles = []
        self.board_size = board_size
        self.last_game_ref = None  # to be set in update_board
        self.create_board()

    def create_board(self):
        for i in range(self.board_size):
            x = 10 + i * 40
            rect = self.create_rectangle(x, 20, x + 35, 55, fill="lightgray")
            text = self.create_text(x + 17, 37, text="", font=("Arial", 10, "bold"))
            self.tiles.append((rect, text))

    def update_board(self, game, flash_index=None, animate=False):
        self.last_game_ref = game
        tile = game.board.head
        survivors = game.get_survivors()

        for i in range(self.board_size):
            occupant = ""
            tile_color = "lightgray"

            # Show active player only if not eliminated
            if tile.occupant and tile.occupant.tile is not None:
                tile_color = "lightblue"
                occupant = tile.occupant.name

                if len(survivors) == 1 and tile.occupant == survivors[0]:
                    occupant = f"🏆{occupant}"

            self.itemconfig(self.tiles[i][0], fill=tile_color)
            self.itemconfig(self.tiles[i][1], text=occupant)
            tile = tile.next

        if flash_index is not None and 0 <= flash_index < len(self.tiles):
            if animate:
                self.animate_tile(flash_index)
            else:
                self.flash_tile(flash_index)

    def flash_tile(self, index):
        if self.last_game_ref is None:
            return

        self.itemconfig(self.tiles[index][0], fill="#ffcc00")
        self.after(300, lambda: self.update_board(self.last_game_ref))

    def animate_tile(self, index):
        if self.last_game_ref is None:
            return

        steps = ["#ffcc00", "#ffdb4d", "#ffe680"]

        def step(i=0):
            if i < len(steps):
                self.itemconfig(self.tiles[index][0], fill=steps[i])
                self.after(100, lambda: step(i + 1))
            else:
                self.update_board(self.last_game_ref)

        step()