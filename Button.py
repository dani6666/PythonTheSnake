class Button:
    def __init__(self, position, size):
        self.is_marked = False
        self.size = size
        self.position = position

    def contains_posision(self, position):
        return position.x>self.position.x and position.x<self.position.x+self.size.x and \
         position.y > self.position.y and position.y < self.position.y + self.size.y