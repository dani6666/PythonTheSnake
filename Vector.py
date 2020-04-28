class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, vector):
        return self.x == vector.x and self.y == vector.y
