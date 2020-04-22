class BodyPiece:

    def __init__(self, pos=(0, 0)):
        self.x = pos[0]
        self.y = pos[1]

    def change_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_pos(self):
        return self.x, self.y
