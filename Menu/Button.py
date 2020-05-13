class Button:
    def __init__(self, position, size):
        self.is_marked = False
        self.size = size
        self.position = position

    def contains_posision(self, position):
        return self.position.x < position.x < self.position.x + self.size.x and \
               self.position.y < position.y < self.position.y + self.size.y
