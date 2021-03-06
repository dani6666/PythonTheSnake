from GameObjects.BodyPiece import BodyPiece
from GameObjects.Head import Head
import copy

from Model.Vector import Vector


class Snake:

    def __init__(self, pos=Vector(0, 0), num=0):
        self.head = Head(pos, num=num)
        self.body = []
        self.grow_pending = False
        self.moving_direction = Vector(1, 0)
        self.num = num

        self.alive = True

    @property
    def position(self):
        return self.head.position

    def move(self):

        previous_head_pos = self.head.move(self.moving_direction)

        if self.body:
            if self.body[-1].fat:
                self.body[-1].fat = False
                self.body.append(copy.deepcopy(self.body[-1]))
            self.body[-1].change_pos(previous_head_pos)
            self.body.insert(0, self.body.pop())

        if self.grow_pending:
            self.grow_pending = False
            if not self.body:
                self.body.append(BodyPiece(previous_head_pos, num=self.num))
            else:
                self.body[0].fat = True

        self.head.move_direction_to_rotation(self.moving_direction)

    def get_slots_occupied_by_body(self):
        return [bp.get_pos() for bp in self.body]

    def get_slots_occupied_by_snake(self):
        return [bp.get_pos() for bp in self.body] + [self.head.position]

    def check_collision(self):
        if self.head.get_pos() in self.get_slots_occupied_by_body():
            return True
        else:
            return False

    def get_size(self):
        return len(self.body) + 1

    def reset(self, head_pos):
        self.head.position = head_pos
        self.body = []
        self.grow_pending = False
        self.moving_direction = Vector(1, 0)

        self.alive = True

    def get_rendering_components(self):
        if self.alive:
            return [bp.get_rendering_components() for bp in self.body] + \
                   [self.head.get_rendering_components()]
        else:
            return []
