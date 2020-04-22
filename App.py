import pygame
import Util
import Snake


class App:

    def __init__(self, window_width=480, window_height=480):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.running = False
        self.dimensions = (window_width, window_height)
        self.grid_size = (window_width // 40, window_height // 40)

        self.moving_direction = (0, 0)
        self.declared_moving_direction = self.moving_direction

        self.snake = Snake.Snake((0, 0))

    def start(self):
        self.running = True
        self.render()
        self.moving_direction = (1, 0)
        self.declared_moving_direction = self.moving_direction

        while self.running:
            self.handle_input()
            self.simulate()
            self.render()

    def handle_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.declared_moving_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.declared_moving_direction = (1, 0)
                elif event.key == pygame.K_UP:
                    self.declared_moving_direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.declared_moving_direction = (0, 1)

    def simulate(self):
        if not Util.is_opposite(self.moving_direction, self.declared_moving_direction):
            self.moving_direction = self.declared_moving_direction

        self.snake.move(self.moving_direction)

        snake_head_pos = self.snake.get_head_pos()
        if snake_head_pos[0] < 0:
            snake_head_pos = (self.grid_size[0] - 1, snake_head_pos[1])
        elif snake_head_pos[1] > self.grid_size[0] - 1:
            snake_head_pos = (0, snake_head_pos[1])

    def render(self):
        self.window.fill((150, 150, 150))

        pass

        pygame.display.update()
