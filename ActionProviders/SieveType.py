import pygame
from Model.Vector import Vector


class SieveType:

    wasd_player = {
        pygame.K_w: Vector(0, -1),
        pygame.K_s: Vector(0, 1),
        pygame.K_a: Vector(-1, 0),
        pygame.K_d: Vector(1, 0)
    }

    arrow_player = {
        pygame.K_UP: Vector(0, -1),
        pygame.K_DOWN: Vector(0, 1),
        pygame.K_LEFT: Vector(-1, 0),
        pygame.K_RIGHT: Vector(1, 0)
    }
