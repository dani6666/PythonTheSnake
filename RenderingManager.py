import pygame

from Vector import Vector


class RenderingManager:
    def __init__(self, window_width, window_height):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Python the Snake")
        self.grid_size = Vector(window_width // 40, window_height // 40)

        self.renderables = []

    def render(self, game_state):
        self.window.fill((150, 150, 150))

        # for renderable in renderables:
        #     for rendering_component in renderable.get_rendering_components():

        sprite = pygame.image.load("resources/apple.png").convert()
        sprite.set_colorkey((255, 0, 255))
        self.window.blit(sprite, (game_state.apple_position.x * 40, game_state.apple_position.y * 40))

        for bp in game_state.snake.body:
            if bp.fat:
                sprite = pygame.image.load("resources/fatbody.png").convert()
            else:
                sprite = pygame.image.load("resources/body.png").convert()
            sprite.set_colorkey((255, 0, 255))
            self.window.blit(sprite, (bp.get_pos().x * 40, bp.get_pos().y * 40))

        sprite = pygame.image.load("resources/head.png").convert()
        sprite.set_colorkey((255, 0, 255))
        if game_state.moving_direction.equals(Vector(0, -1)):
            sprite = pygame.transform.rotate(sprite, 90)
        elif game_state.moving_direction.equals(Vector(-1, 0)):
            sprite = pygame.transform.rotate(sprite, 180)
        elif game_state.moving_direction.equals(Vector(0, 1)):
            sprite = pygame.transform.rotate(sprite, 270)
        self.window.blit(sprite, (game_state.snake.head.get_pos().x * 40, game_state.snake.head.get_pos().y * 40))

        pygame.display.update()
