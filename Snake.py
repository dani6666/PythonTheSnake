from BodyPiece import BodyPiece
from Head import Head
import copy

from Vector import Vector


class Snake:

    def __init__(self, pos=Vector(0, 0)):
        self.head = Head(pos)
        self.body = []
        self.grow_pending = False

    def move(self, moving_direction):

        previous_head_pos = self.head.move(moving_direction)

        if self.grow_pending:
            self.grow_pending = False
            if not self.body:
                self.body.append(BodyPiece(previous_head_pos))
            else:
                self.body[0].fat = True

        if self.body:
            if self.body[-1].fat:
                self.body[-1].fat = False
                self.body.append(copy.deepcopy(self.body[-1]))
            self.body[-1].change_pos(previous_head_pos)
            self.body.insert(0, self.body.pop())

        self.head.move_direction_to_rotation(moving_direction)

    def get_slots_occupied_by_body(self):
        return [bp.get_pos() for bp in self.body]

    def check_collision(self):
        if self.head.get_pos() in self.get_slots_occupied_by_body():
            return True
        else:
            return False

    def get_size(self):
        return len(self.body) + 1

    @staticmethod
    def convert_sprites():
        BodyPiece.convert_sprites()
        Head.convert_sprites()

    def get_rendering_components(self):
        return [self.head.get_rendering_components(), *[bp.get_rendering_components() for bp in self.body]]
