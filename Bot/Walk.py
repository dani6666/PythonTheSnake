from Bot.Strider import Strider
from Model.Vector import Vector


class Walk:

    def __init__(self, starting_position, end_positions, grid_size):
        Strider.destinations = end_positions
        Strider.grid_size = grid_size
        self.grid_size = grid_size
        self.striders = [
            Strider(starting_position, Vector(1, 0)),
            Strider(starting_position, Vector(-1, 0)),
            Strider(starting_position, Vector(0, 1)),
            Strider(starting_position, Vector(0, -1)),

            Strider(starting_position, Vector(1, 1)),
            Strider(starting_position, Vector(1, -1)),
            Strider(starting_position, Vector(-1, 1)),
            Strider(starting_position, Vector(-1, -1)),
        ]

    def walk(self):
        max_breadth = max(self.grid_size.x, self.grid_size.y)
        for i in range(max_breadth):
            for s in self.striders:
                s.stride()
        return [
            s.result if s.result else max_breadth * max_breadth for s in self.striders
        ]
