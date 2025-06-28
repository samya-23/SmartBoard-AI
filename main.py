from game import Game

names = ["A", "B", "C", "D", "E", "F"]
g = Game(board_size=20, player_names=names)

for _ in range(50):
    g.move()
