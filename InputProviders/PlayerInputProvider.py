import pygame

from Model.Vector import Vector


class PlayerInputProvider:
    def retrieve_input(self, game_state):
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
            elif event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
