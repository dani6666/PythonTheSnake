import BodyPiece
from Vector import Vector


class Head(BodyPiece.BodyPiece):

    def move(self, moving_direction=Vector(0, 0)):
        previous_pos = Vector(self.position.x, self.position.y)
        self.position.x += moving_direction.x
        self.position.y += moving_direction.y
        return previous_pos

    def does_collide(self, another_body_piece):
        return self.position.equals(another_body_piece.pos)
