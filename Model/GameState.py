class GameState:

    def __init__(self, grid_size, apple_position, snake, moving_direction, score):
        self.grid_size = grid_size
        self.apple_position =apple_position
        self.snake = snake
        self.moving_direction = moving_direction
        self.score = score
