class Player:
    def __init__(self, name):
        self.name = name
        self.tile = None
        self.next = None
        self.prev = None

class PlayerList:
    def __init__(self):
        self.head = None

    def add_player(self, name):
        new_player = Player(name)
        self._add_to_circle(new_player)

    def add_player_obj(self, player):
        self._add_to_circle(player)

    def _add_to_circle(self, player):
        if not self.head:
            self.head = player
            player.next = player
            player.prev = player
        else:
            tail = self.head.prev
            tail.next = player
            player.prev = tail
            player.next = self.head
            self.head.prev = player