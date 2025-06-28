import tkinter as tk

class BoardView(tk.Canvas):
    def __init__(self, root, board_size):
        super().__init__(root, width=40 * board_size + 20, height=100, bg="white")
        self.tiles = []
        self.board_size = board_size
        self.create_board()

    def create_board(self):
        for i in range(self.board_size):
            x = 10 + i * 40
            rect = self.create_rectangle(x, 20, x + 35, 55, fill="lightgray")
            text = self.create_text(x + 17, 37, text="", font=("Arial", 10, "bold"))
            self.tiles.append((rect, text))

    def update_board(self, game):
        tile = game.board.head
        for i in range(self.board_size):
            occupant = tile.occupant.name if tile.occupant else ""
            self.itemconfig(self.tiles[i][1], text=occupant)
            tile = tile.next
