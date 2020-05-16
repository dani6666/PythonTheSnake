import pygame

from Model.Vector import Vector


class PlayerInputProvider:

    @staticmethod
    def retrieve_input():
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return Vector(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    return Vector(1, 0)
                elif event.key == pygame.K_UP:
                    return Vector(0, -1)
                elif event.key == pygame.K_DOWN:
                    return Vector(0, 1)
