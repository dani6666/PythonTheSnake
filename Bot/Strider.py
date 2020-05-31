from Model.Vector import Vector
import copy


class Strider:
    grid_size = None
    destinations = None

    def __init__(self, position, moving_direction):
        self.position = copy.copy(position)
        self.starting_position = copy.copy(position)
        self.moving_direction = moving_direction
        self.distance = 0
        self.diagonal = (int(moving_direction) == 2)

        self.result = None

    def stride(self):
        if self.result:
            return

        self.position += self.moving_direction
        self.distance += 1

        if self.position.x < 0:
            self.position.x = Strider.grid_size.x - 1
        elif self.position.x == Strider.grid_size.x:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = Strider.grid_size.y - 1
        elif self.position.y == Strider.grid_size.y:
            self.position.y = 0

        if self.position in Strider.destinations:
            self.result = self.distance * int(self.moving_direction)

        if self.diagonal and not self.result:
            minimal_distance = None
            for i in range(1, self.distance + 1):
                if \
                        Vector((self.position.x - i * self.moving_direction.x) % Strider.grid_size.x, self.position.y) \
                        in Strider.destinations \
                        or \
                        Vector(self.position.x, (self.position.y - i * self.moving_direction.y) % Strider.grid_size.y) \
                        in Strider.destinations:
                    minimal_distance = self.distance * 2 - i
            if minimal_distance:
                self.result = minimal_distance


def test():

    Strider.grid_size = Vector(5, 5)
    Strider.destinations = [Vector(2, 2)]

    # correct distance in a line
    strider = Strider(Vector(0, 2), Vector(1, 0))
    strider.stride()
    strider.stride()
    strider.stride()
    print("Distance from (0, 2) to (2, 2) right is 2:", strider.result == 2)

    # same backwards
    strider = Strider(Vector(0, 2), Vector(-1, 0))
    strider.stride()
    strider.stride()
    strider.stride()
    strider.stride()
    print("Distance from (0, 2) to (2, 2) left is 3:", strider.result == 3)

    # correct distance in diagonal
    strider = Strider(Vector(0, 0), Vector(1, 1))
    strider.stride()
    strider.stride()
    strider.stride()
    print("Distance from (0, 0) to (2, 2) diagonal is 4:", strider.result == 4)

    # same backwards
    strider = Strider(Vector(0, 0), Vector(-1, -1))
    strider.stride()
    strider.stride()
    strider.stride()
    strider.stride()
    print("Distance from (0, 0) to (2, 2) diagonal backwards is 6:", strider.result == 6)

    strider = Strider(Vector(0, 1), Vector(1, 1))
    strider.stride()
    strider.stride()
    strider.stride()
    strider.stride()
    print("Distance from (0, 1) to (2, 2) diagonal is 3:", strider.result == 3)


if __name__ == "__main__":
    test()
