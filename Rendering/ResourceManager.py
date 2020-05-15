import pygame


class ResourceManager:
    snake_head = pygame.image.load("resources/head.png")
    snake_body = pygame.image.load("resources/body.png")
    snake_fat_body = pygame.image.load("resources/fatbody.png")
    apple = pygame.image.load("resources/apple.png")
    text_font = None

    @staticmethod
    def initialize_font():
        ResourceManager.text_font = pygame.font.Font(None, 30)

    @staticmethod
    def convert_resources():
        ResourceManager.snake_head = ResourceManager.snake_head.convert()
        ResourceManager.snake_head.set_colorkey((255, 0, 255))
        ResourceManager.snake_body = ResourceManager.snake_body.convert()
        ResourceManager.snake_body.set_colorkey((255, 0, 255))
        ResourceManager.snake_fat_body = ResourceManager.snake_fat_body.convert()
        ResourceManager.snake_fat_body.set_colorkey((255, 0, 255))
        ResourceManager.apple = ResourceManager.apple.convert()
        ResourceManager.apple.set_colorkey((255, 0, 255))

