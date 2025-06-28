class Player:
    def __init__(self, name):
        self.name = name
        self.tile = None
        self.next = None

class PlayerList:
    def __init__(self):
        self.head = None

    def add_player(self, name):
        new_player = Player(name)
        if not self.head:
            self.head = new_player
            new_player.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_player
            new_player.next = self.head
