def is_opposite(tup1, tup2):
    if (tup1[0] == -tup2[0] and tup1[1] == tup2[1]) or \
            (tup1[1] == -tup2[1] and tup1[0] == tup2[0]):
        return True
    return False
