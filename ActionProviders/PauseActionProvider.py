import pygame


class PauseActionProvider:

    @staticmethod
    def check_pause(events):
        return pygame.K_SPACE in [e.key for e in events]
