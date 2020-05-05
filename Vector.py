class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, vector):
        return self.x == vector.x and self.y == vector.y

    def to_tup(self):
        return self.x, self.y

    def in_vector_list(self, v_list):
        for v in v_list:
            if self.equals(v):
                return True
        return False
