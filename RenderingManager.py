import pygame

from Vector import Vector


class RenderingManager:
    def __init__(self, window_width, window_height):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Python the Snake")
        self.grid_size = Vector(window_width // 40, window_height // 40)
        self.apple_sprite = pygame.image.load("resources/apple.png").convert()
        self.apple_sprite.set_colorkey((255, 0, 255))
        self.body_sprite = pygame.image.load("resources/body.png").convert()
        self.body_sprite.set_colorkey((255, 0, 255))
        self.fat_body_sprite = pygame.image.load("resources/fatbody.png").convert()
        self.fat_body_sprite.set_colorkey((255, 0, 255))
        self.head_sprite = pygame.image.load("resources/head.png").convert()
        self.head_sprite.set_colorkey((255, 0, 255))

    def render_board(self, game_state):
        self.window.fill((150, 150, 150))

        self.window.blit(self.apple_sprite, (game_state.apple_position.x * 40, game_state.apple_position.y * 40))

        for bp in game_state.snake.body:
            if bp.fat:
                self.window.blit(self.fat_body_sprite, (bp.get_pos().x * 40, bp.get_pos().y * 40))
            else:
                self.window.blit(self.body_sprite, (bp.get_pos().x * 40, bp.get_pos().y * 40))

        sprite_position = (game_state.snake.head.get_pos().x * 40, game_state.snake.head.get_pos().y * 40)
        if game_state.moving_direction == Vector(0, -1):
            self.window.blit(pygame.transform.rotate(self.head_sprite, 90), sprite_position)
        elif game_state.moving_direction == Vector(-1, 0):
            self.window.blit(pygame.transform.rotate(self.head_sprite, 180), sprite_position)
        elif game_state.moving_direction == Vector(0, 1):
            self.window.blit(pygame.transform.rotate(self.head_sprite, 270), sprite_position)
        else:
            self.window.blit(self.head_sprite, sprite_position)

        pygame.display.update()
