import pygame


class QuitInputProvider:
    def check_quit(self):
        events = pygame.event.peek(pygame.QUIT)
        if events != 0:
            pygame.quit()
