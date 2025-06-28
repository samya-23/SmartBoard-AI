from player import Player

class AIPlayer(Player):
    def __init__(self, name="BOT"):
        super().__init__(name)
        self.is_ai = True

    def move(self, return_reason=False):
        if not self.tile:
            reason = f"{self.name} (AI) is eliminated. Skipping turn."
            print(reason)
            if return_reason:
                return {
                    "index": None,
                    "reason": reason,
                    "next_pos": None,
                    "jumped_name": None,
                    "action": "Eliminated"
                }
            return None

        current_pos = self.tile.position
        best = self.get_best_move(self.tile, depth=2)

        if best:
            jump_tile, remove_tile = best
            jumped_name = remove_tile.occupant.name if remove_tile.occupant else "?"
            self.tile.occupant = None
            remove_tile.occupant = None
            jump_tile.occupant = self
            self.tile = jump_tile

            reason = f"Jumped over {jumped_name} to Tile {jump_tile.position}"
            print(f"{self.name} (AI) {reason}")

            if return_reason:
                return {
                    "index": jump_tile.position,
                    "reason": reason,
                    "next_pos": jump_tile.position,
                    "jumped_name": jumped_name,
                    "action": "Jump"
                }
            return jump_tile.position

        if self.tile.next and not self.tile.next.occupant:
            self.move_forward()
            reason = f"Moved forward to Tile {self.tile.position}"
            print(f"{self.name} (AI) {reason}")
            if return_reason:
                return {
                    "index": self.tile.position,
                    "reason": reason,
                    "next_pos": self.tile.position,
                    "jumped_name": None,
                    "action": "Move Forward"
                }
            return self.tile.position

        reason = f"Blocked at Tile {current_pos}. No valid moves."
        print(f"{self.name} (AI) {reason}")
        if return_reason:
            return {
                "index": current_pos,
                "reason": reason,
                "next_pos": current_pos,
                "jumped_name": None,
                "action": "Blocked"
            }
        return current_pos

    def get_best_move(self, tile, depth):
        best_score = float('-inf')
        best_move = None
        for move in self.get_valid_jumps(tile):
            score = self.simulate_move(tile, move, depth)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def simulate_move(self, tile, move, depth):
        if depth == 0:
            return 1
        jump_tile, remove_tile = move
        original_tile_occupant = tile.occupant
        original_jump_occupant = jump_tile.occupant
        original_remove_occupant = remove_tile.occupant

        tile.occupant = None
        remove_tile.occupant = None
        jump_tile.occupant = self

        future_jumps = self.get_valid_jumps(jump_tile)
        future_scores = [self.simulate_move(jump_tile, m, depth - 1) for m in future_jumps] or [0]
        score = 1 + max(future_scores)

        tile.occupant = original_tile_occupant
        jump_tile.occupant = original_jump_occupant
        remove_tile.occupant = original_remove_occupant

        return score

    def get_valid_jumps(self, tile):
        moves = []
        if tile.next and tile.next.occupant and tile.next.next and not tile.next.next.occupant:
            moves.append((tile.next.next, tile.next))
        if tile.prev and tile.prev.occupant and tile.prev.prev and not tile.prev.prev.occupant:
            moves.append((tile.prev.prev, tile.prev))
        return moves

    def move_forward(self):
        if self.tile and self.tile.next and not self.tile.next.occupant:
            self.tile.occupant = None
            self.tile.next.occupant = self
            self.tile = self.tile.next