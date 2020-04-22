import BodyPiece


class Head(BodyPiece.BodyPiece):

    def move(self, moving_direction=(0, 0)):
        previous_pos = self.pos
        self.pos[0] += moving_direction[0]
        self.pos[1] += moving_direction[1]
        return previous_pos

    def does_collide(self, another_body_piece):
        if another_body_piece.pos[0] == self.pos[0] and another_body_piece.pos[1] == self.pos[1]:
            return True
        return False
