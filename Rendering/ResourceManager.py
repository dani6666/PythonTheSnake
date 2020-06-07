import pygame


class ResourceManager:

    snake_heads = []
    for i in range(4):
        snake_heads.append(pygame.image.load("resources/head" + str(i) + ".png"))
    snake_bodies = []
    for i in range(4):
        snake_bodies.append(pygame.image.load("resources/body" + str(i) + ".png"))
    snake_fatbodies = []
    for i in range(4):
        snake_fatbodies.append(pygame.image.load("resources/fatbody" + str(i) + ".png"))
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
    button_resume = pygame.image.load("resources/resume.png")

    msg_win = pygame.image.load("resources/you_win.png")
    msg_lose = pygame.image.load("resources/game_over.png")
    msg_px_wins = []
    for i in range(1, 5):
        msg_px_wins.append(pygame.image.load("resources/p" + str(i) + "_wins.png"))
    msg_tie = pygame.image.load("resources/tie.png")
    msg_pause = pygame.image.load("resources/pause.png")

    @staticmethod
    def initialize_font():
        ResourceManager.text_font = pygame.font.Font(None, 30)

    @staticmethod
    def convert_resources():
        for i in range(4):
            ResourceManager.snake_heads[i] = ResourceManager.snake_heads[i].convert()
            ResourceManager.snake_heads[i].set_colorkey((255, 0, 255))
        for i in range(4):
            ResourceManager.snake_bodies[i] = ResourceManager.snake_bodies[i].convert()
            ResourceManager.snake_bodies[i].set_colorkey((255, 0, 255))
        for i in range(4):
            ResourceManager.snake_fatbodies[i] = ResourceManager.snake_fatbodies[i].convert()
            ResourceManager.snake_fatbodies[i].set_colorkey((255, 0, 255))
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
        ResourceManager.button_resume = ResourceManager.button_resume.convert()
        ResourceManager.button_resume.set_colorkey((255, 0, 255))

        ResourceManager.msg_win = ResourceManager.msg_win.convert()
        ResourceManager.msg_win.set_colorkey((255, 0, 255))
        ResourceManager.msg_lose = ResourceManager.msg_lose.convert()
        ResourceManager.msg_lose.set_colorkey((255, 0, 255))
        for i in range(4):
            ResourceManager.msg_px_wins[i] = ResourceManager.msg_px_wins[i].convert()
            ResourceManager.msg_px_wins[i].set_colorkey((255, 0, 255))
        ResourceManager.msg_tie = ResourceManager.msg_tie.convert()
        ResourceManager.msg_tie.set_colorkey((255, 0, 255))
        ResourceManager.msg_pause = ResourceManager.msg_pause.convert()
        ResourceManager.msg_pause.set_colorkey((255, 0, 255))

    @staticmethod
    def initialize_score_bar(width):
        ResourceManager.info_bar = pygame.Surface((width, 40))
        ResourceManager.info_bar.fill((0, 0, 0))
        ResourceManager.info_bar = ResourceManager.info_bar.convert()
