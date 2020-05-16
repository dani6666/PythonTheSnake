import pygame


class ResourceManager:

    snake_head = pygame.image.load("resources/head.png")
    snake_body = pygame.image.load("resources/body.png")
    snake_fat_body = pygame.image.load("resources/fatbody.png")
    apple = pygame.image.load("resources/apple.png")
    button_inactive = pygame.image.load("resources/button_inactive.png")
    text_font = None

    digits = list()
    for i in range(10):
        digits.append(pygame.image.load("resources/" + str(i) + ".png"))
    colon = pygame.image.load("resources/colon.png")
    info_bar = None

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
        ResourceManager.button_inactive = ResourceManager.button_inactive.convert()
        ResourceManager.button_inactive.set_colorkey((255, 0, 255))

        for i in range(10):
            ResourceManager.digits[i] = ResourceManager.digits[i].convert()
            ResourceManager.digits[i].set_colorkey((255, 0, 255))
        ResourceManager.colon = ResourceManager.colon.convert()
        ResourceManager.colon.set_colorkey((255, 0, 255))

    @staticmethod
    def initialize_score_bar(width):
        ResourceManager.info_bar = pygame.Surface((width, 40))
        ResourceManager.info_bar.fill((0, 0, 0))
        ResourceManager.info_bar = ResourceManager.info_bar.convert()
