class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not other:
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __floordiv__(self, other):
        return Vector(self.x // other.x, self.y // other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def to_tup(self):
        return self.x, self.y

    def __int__(self):
        return abs(self.x) + abs(self.y)
