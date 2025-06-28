from board import Board
from player import PlayerList
from ai_bot import AIPlayer

class Game:
    def __init__(self, board_size, player_names):
        self.original_names = player_names
        self.board_size = board_size
        self.total_players = len(player_names)
        self.eliminated = {}
        self.last_bot_decision = ""
        self.winner = None
        self.current = None
        self._init_game()

    def _init_game(self):
        self.board = Board(self.board_size)
        self.players = PlayerList()
        self.eliminated = {}
        self.last_bot_decision = ""
        self.winner = None

        for name in self.original_names:
            if name.upper() == "BOT":
                self.players.add_player_obj(AIPlayer(name))
            else:
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
        if self.is_game_over():
            return None

        survivors = self.get_survivors()
        while self.current.tile is None:
            self.current = self.current.next
            if self.current not in survivors:
                return None

        player = self.current
        current_tile = player.tile
        jump_to = None
        self.last_bot_decision = ""

        print(f"\n{player.name}'s turn at Tile {current_tile.position if current_tile else 'N/A'}")

        if hasattr(player, "is_ai") and player.is_ai:
            prev_tile = player.tile
            move_info = player.move(return_reason=True)

            # If AI jumped someone, register them as eliminated
            if move_info.get("jumped_name") and move_info.get("action") == "Jump":
                jumped_name = move_info["jumped_name"]
                jumped_player = next((p for p in self.get_survivors() if p.name == jumped_name), None)
                if jumped_player:
                    self.eliminated[jumped_player.name] = jumped_player.tile
                    jumped_player.tile.occupant = None
                    jumped_player.tile = None

            if player.tile and player.tile != prev_tile:
                jump_to = player.tile.position

            self.last_bot_decision = (
                f"🤖 BOT Strategy:\n"
                f"- Current: {prev_tile.position if prev_tile else 'N/A'}\n"
                f"- Next: {move_info.get('next_pos', 'N/A')}\n"
                f"- Jumped: {move_info.get('jumped_name', 'None')}\n"
                f"- Action: {move_info.get('action', 'Unknown')}"
            )

        else:
            if current_tile.next and current_tile.next.occupant:
                if current_tile.next.next and not current_tile.next.next.occupant:
                    jumped = current_tile.next.occupant
                    self.eliminated[jumped.name] = current_tile.next
                    current_tile.occupant = None
                    current_tile.next.occupant = None
                    jumped.tile = None
                    print(f"{player.name} jumps over {jumped.name}")
                    current_tile.next.next.occupant = player
                    player.tile = current_tile.next.next
                    jump_to = current_tile.next.next.position
            elif current_tile.next and not current_tile.next.occupant:
                current_tile.occupant = None
                current_tile.next.occupant = player
                player.tile = current_tile.next
                jump_to = current_tile.next.position
            else:
                print(f"{player.name} cannot move")

        # Skip to next active player
        next_player = self.current.next
        checked = 0
        while next_player.tile is None and checked < self.total_players:
            next_player = next_player.next
            checked += 1
        self.current = next_player

        return jump_to


    def is_game_over(self):
        survivors = self.get_survivors()

        if len(survivors) == 1:
            self.winner = survivors[0]
            return True

        if len(survivors) == 0:
            self.winner = None
            return True

        for player in survivors:
            t = player.tile
            if t and (
                (t.next and not t.next.occupant) or
                (t.next and t.next.next and t.next.occupant and not t.next.next.occupant)
            ):
                return False

        self.winner = None
        return True

    def get_survivors(self):
        survivors = []
        current = self.players.head
        visited = set()
        while current and current not in visited:
            visited.add(current)
            if current.tile is not None:
                survivors.append(current)
            current = current.next
        return survivors

    def get_eliminated_players(self):
        eliminated_players = []
        current = self.players.head
        visited = set()
        while current and current not in visited:
            visited.add(current)
            if current.tile is None:
                eliminated_players.append(current)
            current = current.next
        return eliminated_players

    def reset(self):
        print("\nRestarting game...\n")
        self.eliminated.clear()
        self.last_bot_decision = ""
        self.winner = None
        self._init_game()