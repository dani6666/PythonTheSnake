class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def to_tup(self):
        return self.x, self.y

    def divide(self, divide_vector):
        return Vector(self.x // divide_vector.x, self.y // divide_vector.y)
