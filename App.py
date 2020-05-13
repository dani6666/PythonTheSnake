from GameInitializer import GameInitializer
from Menu.MainMenuWindow import MainMenuWindow
from MenuClock import MenuClock
from InputProviders.MouseInputProvider import MouseInputProvider
from Rendering.RenderingManager import RenderingManager
import pygame


class App:

    def start(self):
        pygame.init()
        input_provider = MouseInputProvider()
        menu_manager = MainMenuWindow()
        rendering_manager = RenderingManager()
        rendering_manager.add_action_frame(menu_manager.get_action_frame())
        game_intializer = GameInitializer()
        clock = MenuClock(input_provider, menu_manager, rendering_manager, game_intializer)

        clock.start_app()
