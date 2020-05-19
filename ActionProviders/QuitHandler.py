import pygame


class QuitHandler:

    @staticmethod
    def check_quit():
        events = pygame.event.peek(pygame.QUIT)
        if events != 0:
            pygame.quit()
            exit()
