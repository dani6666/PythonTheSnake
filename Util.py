def is_opposite(tup1, tup2):
    return (tup1.x == -tup2.x and tup1.y == tup2.y) or (tup1.y == -tup2.y and tup1.x == tup2.x)
