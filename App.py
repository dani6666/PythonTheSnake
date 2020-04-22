import pygame
import Util
import Snake
import random


class App:

    def __init__(self, window_width=480, window_height=480):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.running = False
        self.dimensions = (window_width, window_height)
        self.grid_size = (window_width // 40, window_height // 40)

        self.moving_direction = (1, 0)
        self.declared_moving_direction = self.moving_direction

        snake_pos = (random.randrange(self.grid_size[0]), random.randrange(self.grid_size[1]))
        self.snake = Snake.Snake(snake_pos)
        apple_pos = (random.randrange(self.grid_size[0]), random.randrange(self.grid_size[1]))
        while apple_pos == snake_pos:
            apple_pos = (random.randrange(self.grid_size[0]), random.randrange(self.grid_size[1]))

        self.apple_pos = apple_pos

    def start(self):
        self.running = True
        self.render()
        self.declared_moving_direction = self.moving_direction

        clock = pygame.time.Clock()

        while self.running:
            pygame.time.delay(100)
            clock.tick(10)

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
            elif event.type == pygame.QUIT:
                self.running = False

    def simulate(self):

        if not Util.is_opposite(self.moving_direction, self.declared_moving_direction):
            self.moving_direction = self.declared_moving_direction

        self.snake.move(self.moving_direction)

        # crossing border
        snake_head_pos = self.snake.get_head_pos()
        if snake_head_pos[0] < 0:
            self.snake.head.change_pos((self.grid_size[0] - 1, snake_head_pos[1]))
        elif snake_head_pos[0] > self.grid_size[0] - 1:
            self.snake.head.change_pos((0, snake_head_pos[1]))
        elif snake_head_pos[1] < 0:
            self.snake.head.change_pos((snake_head_pos[0], self.grid_size[1] - 1))
        elif snake_head_pos[1] > self.grid_size[1] - 1:
            self.snake.head.change_pos((snake_head_pos[0], 0))

        # eating apple
        if snake_head_pos == self.apple_pos:
            self.snake.grow()

            if self.snake.get_size() == self.grid_size[0] * self.grid_size[1] - 1:
                self.running = False

            while self.apple_pos in self.snake.get_slots_occupied_by_body() or \
                    self.apple_pos == self.snake.get_head_pos():
                self.apple_pos = (random.randrange(self.grid_size[0]), random.randrange(self.grid_size[1]))

        # checking self collision
        if self.snake.check_collision():
            self.running = False

    def render(self):
        self.window.fill((150, 150, 150))

        sprite = pygame.image.load("resources/head.png").convert()
        sprite.set_colorkey((255, 0, 255))
        self.window.blit(sprite, (self.snake.get_head_pos()[0] * 40, self.snake.get_head_pos()[1] * 40))

        sprite = pygame.image.load("resources/apple.png").convert()
        sprite.set_colorkey((255, 0, 255))
        self.window.blit(sprite, (self.apple_pos[0] * 40, self.apple_pos[1] * 40))

        for bp in self.snake.get_slots_occupied_by_body():
            sprite = pygame.image.load("resources/body.png").convert()
            sprite.set_colorkey((255, 0, 255))
            self.window.blit(sprite, (bp[0] * 40, bp[1] * 40))

        pygame.display.update()
