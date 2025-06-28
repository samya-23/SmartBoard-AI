from board import Board
from player import PlayerList

class Game:
    def __init__(self, board_size, player_names):
        self.board = Board(board_size)
        self.players = PlayerList()
        for name in player_names:
            self.players.add_player(name)
        self.current = self.players.head
        self.place_players()

    def place_players(self):
        tile = self.board.head
        curr = self.players.head
        while True:
            tile.occupant = curr
            curr.tile = tile
            tile = tile.next
            curr = curr.next
            if curr == self.players.head:
                break

    def move(self):
        player = self.current
        current_tile = player.tile

        if current_tile is None:
            print(f"\n{player.name} has been jumped and is out of the game.")
            self.current = self.current.next
            return

        print(f"\n{player.name}'s turn at Tile {current_tile.position}")
        if current_tile.next and current_tile.next.occupant:
            # Jump logic: if next tile has someone, check 2 tiles ahead
            if current_tile.next.next and not current_tile.next.next.occupant:
                jumped = current_tile.next.occupant
                # Dancing Links-like remove
                current_tile.occupant = None
                current_tile.next.occupant = None
                jumped.tile = None
                print(f"{player.name} jumps over {jumped.name}")
                current_tile.next.next.occupant = player
                player.tile = current_tile.next.next
        elif current_tile.next and not current_tile.next.occupant:
            # Simple move forward
            current_tile.occupant = None
            current_tile.next.occupant = player
            player.tile = current_tile.next
        else:
            print(f"{player.name} cannot move")
        self.current = self.current.next
