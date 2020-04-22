class BodyPiece:

    def __init__(self, pos=(0, 0)):
        self.pos = pos

    def change_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos
