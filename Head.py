import BodyPiece


class Head(BodyPiece.BodyPiece):

    def move(self, moving_direction=(0, 0)):
        previous_pos = (self.x, self.y)
        self.x += moving_direction[0]
        self.y += moving_direction[1]
        return previous_pos

    def does_collide(self, another_body_piece):
        if another_body_piece.pos[0] == self.x and another_body_piece.pos[1] == self.y:
            return True
        return False
