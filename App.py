import pygame
import Util
import Snake
import random

from GameClock import GameClock
from GameManager import GameManager
from PlayerInputProvider import PlayerInputProvider
from RenderingManager import RenderingManager
from Vector import Vector


class App:

    def start(self):
        input_provider = PlayerInputProvider()
        game_manager = GameManager(Vector(12, 12))
        rendering_manager = RenderingManager(12*40, 12*40)
        clock = GameClock(input_provider, game_manager, rendering_manager)

        clock.start_game()
