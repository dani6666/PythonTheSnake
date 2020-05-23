import pygame
from Model.Vector import Vector


class SieveType:

    arrow_player = {
        pygame.K_UP: Vector(0, -1),
        pygame.K_DOWN: Vector(0, 1),
        pygame.K_LEFT: Vector(-1, 0),
        pygame.K_RIGHT: Vector(1, 0)
    }

    wasd_player = {
        pygame.K_w: Vector(0, -1),
        pygame.K_s: Vector(0, 1),
        pygame.K_a: Vector(-1, 0),
        pygame.K_d: Vector(1, 0)
    }

    ijkl_player = {
        pygame.K_i: Vector(0, -1),
        pygame.K_k: Vector(0, 1),
        pygame.K_j: Vector(-1, 0),
        pygame.K_l: Vector(1, 0)
    }

    num_player = {
        pygame.K_KP8: Vector(0, -1),
        pygame.K_KP5: Vector(0, 1),
        pygame.K_KP4: Vector(-1, 0),
        pygame.K_KP6: Vector(1, 0)
    }
