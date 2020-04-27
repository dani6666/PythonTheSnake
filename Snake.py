import BodyPiece
import Head
import copy

from Vector import Vector


class Snake:

    def __init__(self, pos=Vector(0, 0)):
        self.head = Head.Head(pos)
        self.body = []
        self.grow_pending = False

    def move(self, moving_direction):

        previous_head_pos = self.head.move(moving_direction)

        if self.grow_pending:
            self.grow_pending = False
            if not self.body:
                self.body.append(BodyPiece.BodyPiece(previous_head_pos))
            else:
                self.body[0].fat = True

        if self.body:
            if self.body[-1].fat:
                self.body[-1].fat = False
                self.body.append(copy.deepcopy(self.body[-1]))
            self.body[-1].change_pos(previous_head_pos)
            self.body.insert(0, self.body.pop())

    def get_slots_occupied_by_body(self):
        return [bp.get_pos() for bp in self.body]

    def check_collision(self):
        if self.head.get_pos() in [bp.get_pos() for bp in self.body]:
            return True
        else:
            return False

    def get_size(self):
        return len(self.body) + 1
