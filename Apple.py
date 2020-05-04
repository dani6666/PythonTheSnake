from Vector import Vector
import pygame


class Apple:

    # sprite = pygame.image.load("resources/apple.png").convert()
    # sprite.set_colorkey((255, 0, 255))

    def __init__(self, position=Vector(0, 0)):
        self.position = position
        self.fat = False

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position
