class GameResult:
    def __init__(self, score, moves, was_snake_idle):
        self.score = score
        self.moves = moves
        self.was_snake_idle = was_snake_idle

    def __eq__(self, other):
        return self.score == other.score and self.moves == other.moves and self.was_snake_idle == other.was_snake_idle

    def __lt__(self, other):
        if self.score == other.score:
            return self.moves > other.moves
        return self.score < other.score

    def __le__(self, other):
        if self.score == other.score:
            return self.moves >= other.moves
        return self.score < other.score

    def __ne__(self, other):
        return self.score != other.score or self.moves != other.moves or self.was_snake_idle != other.was_snake_idle

    def __ge__(self, other):
        if self.score == other.score:
            return self.moves <= other.moves
        return self.score > other.score

    def __gt__(self, other):
        if self.score == other.score:
            return self.moves < other.moves
        return self.score > other.score
