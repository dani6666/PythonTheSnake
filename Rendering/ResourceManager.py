import pygame


class ResourceManager:

    snake_head0 = pygame.image.load("resources/head0.png")
    snake_body0 = pygame.image.load("resources/body0.png")
    snake_fat_body0 = pygame.image.load("resources/fatbody0.png")
    snake_head1 = pygame.image.load("resources/head1.png")
    snake_body1 = pygame.image.load("resources/body1.png")
    snake_fat_body1 = pygame.image.load("resources/fatbody1.png")
    apple = pygame.image.load("resources/apple.png")
    button_inactive = pygame.image.load("resources/button_inactive.png")
    text_font = None

    digits = list()
    for i in range(10):
        digits.append(pygame.image.load("resources/" + str(i) + ".png"))
    colon = pygame.image.load("resources/colon.png")
    info_bar = None
    button_back = pygame.image.load("resources/back.png")
    button_retry = pygame.image.load("resources/retry.png")

    msg_win = pygame.image.load("resources/you_win.png")
    msg_lose = pygame.image.load("resources/game_over.png")
    msg_p1_wins = pygame.image.load("resources/p1_wins.png")
    msg_p2_wins = pygame.image.load("resources/p2_wins.png")
    msg_tie = pygame.image.load("resources/tie.png")

    @staticmethod
    def initialize_font():
        ResourceManager.text_font = pygame.font.Font(None, 30)

    @staticmethod
    def convert_resources():
        ResourceManager.snake_head0 = ResourceManager.snake_head0.convert()
        ResourceManager.snake_head0.set_colorkey((255, 0, 255))
        ResourceManager.snake_body0 = ResourceManager.snake_body0.convert()
        ResourceManager.snake_body0.set_colorkey((255, 0, 255))
        ResourceManager.snake_fat_body0 = ResourceManager.snake_fat_body0.convert()
        ResourceManager.snake_fat_body0.set_colorkey((255, 0, 255))
        ResourceManager.snake_head1 = ResourceManager.snake_head1.convert()
        ResourceManager.snake_head1.set_colorkey((255, 0, 255))
        ResourceManager.snake_body1 = ResourceManager.snake_body1.convert()
        ResourceManager.snake_body1.set_colorkey((255, 0, 255))
        ResourceManager.snake_fat_body1 = ResourceManager.snake_fat_body1.convert()
        ResourceManager.snake_fat_body1.set_colorkey((255, 0, 255))
        ResourceManager.apple = ResourceManager.apple.convert()
        ResourceManager.apple.set_colorkey((255, 0, 255))
        ResourceManager.button_inactive = ResourceManager.button_inactive.convert()
        ResourceManager.button_inactive.set_colorkey((255, 0, 255))

        for i in range(10):
            ResourceManager.digits[i] = ResourceManager.digits[i].convert()
            ResourceManager.digits[i].set_colorkey((255, 0, 255))

        ResourceManager.colon = ResourceManager.colon.convert()
        ResourceManager.colon.set_colorkey((255, 0, 255))
        ResourceManager.button_back = ResourceManager.button_back.convert()
        ResourceManager.button_back.set_colorkey((255, 0, 255))
        ResourceManager.button_retry = ResourceManager.button_retry.convert()
        ResourceManager.button_retry.set_colorkey((255, 0, 255))

        ResourceManager.msg_win = ResourceManager.msg_win.convert()
        ResourceManager.msg_win.set_colorkey((255, 0, 255))
        ResourceManager.msg_lose = ResourceManager.msg_lose.convert()
        ResourceManager.msg_lose.set_colorkey((255, 0, 255))
        ResourceManager.msg_p1_wins = ResourceManager.msg_p1_wins.convert()
        ResourceManager.msg_p1_wins.set_colorkey((255, 0, 255))
        ResourceManager.msg_p2_wins = ResourceManager.msg_p2_wins.convert()
        ResourceManager.msg_p2_wins.set_colorkey((255, 0, 255))
        ResourceManager.msg_tie = ResourceManager.msg_tie.convert()
        ResourceManager.msg_tie.set_colorkey((255, 0, 255))

    @staticmethod
    def initialize_score_bar(width):
        ResourceManager.info_bar = pygame.Surface((width, 40))
        ResourceManager.info_bar.fill((0, 0, 0))
        ResourceManager.info_bar = ResourceManager.info_bar.convert()
