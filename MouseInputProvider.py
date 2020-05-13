import pygame

from Vector import Vector


class PlayerInputProvider:
    def get_click_position(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.key == pygame.BUTTON_LEFT:
                mouse_position = pygame.mouse.get_pos()
                return Vector(mouse_position[0], mouse_position[1])
            elif event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
