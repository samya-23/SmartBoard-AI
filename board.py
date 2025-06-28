class Tile:
    def __init__(self, position):
        self.position = position
        self.prev = None
        self.next = None
        self.occupant = None  # Reference to the player on this tile

class Board:
    def __init__(self, size):
        self.head = Tile(0)
        current = self.head
        for i in range(1, size):
            new_tile = Tile(i)
            current.next = new_tile
            new_tile.prev = current
            current = new_tile
        # Optional: Make board circular if needed (can be commented if linear)
        # current.next = self.head
        # self.head.prev = current