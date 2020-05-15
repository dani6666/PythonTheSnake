import pygame


class ResourceManager:
    snake_head = pygame.image.load("resources/head.png")
    snake_body = pygame.image.load("resources/body.png")
    snake_fat_body = pygame.image.load("resources/fatbody.png")
    apple = pygame.image.load("resources/apple.png")
    text_font = None

    digits = list()
    digits.append(pygame.image.load("resources/0.png"))
    digits.append(pygame.image.load("resources/1.png"))
    digits.append(pygame.image.load("resources/2.png"))
    digits.append(pygame.image.load("resources/3.png"))
    digits.append(pygame.image.load("resources/4.png"))
    digits.append(pygame.image.load("resources/5.png"))
    digits.append(pygame.image.load("resources/6.png"))
    digits.append(pygame.image.load("resources/7.png"))
    digits.append(pygame.image.load("resources/8.png"))
    digits.append(pygame.image.load("resources/9.png"))
    score_bar = None

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

        for i in range(10):
            ResourceManager.digits[i] = ResourceManager.digits[i].convert()
            ResourceManager.digits[i].set_colorkey((255, 0, 255))

    @staticmethod
    def initialize_score_bar(width):
        ResourceManager.score_bar = pygame.Surface((width, 40))
        ResourceManager.score_bar.fill((50, 50, 50))
        ResourceManager.score_bar = ResourceManager.score_bar.convert()

