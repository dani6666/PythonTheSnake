from GameInitializer import GameInitializer
from Menu.MainMenuWindow import MainMenuWindow
from MenuClock import MenuClock
from ActionProviders.MouseActionProvider import MouseActionProvider
from Rendering.RenderingManager import RenderingManager
import pygame

from Rendering.ResourceManager import ResourceManager


class App:

    @staticmethod
    def start():
        pygame.init()
        pygame.font.init()
        pygame.display.set_mode((1, 1))
        ResourceManager.initialize_font()
        ResourceManager.convert_resources()
        input_provider = MouseActionProvider()
        menu_manager = MainMenuWindow()
        RenderingManager.add_action_frame(menu_manager.get_action_frame())
        game_intializer = GameInitializer()
        clock = MenuClock(input_provider, menu_manager, game_intializer)

        while True:
            clock.start_app()
            menu_manager = MainMenuWindow()
            RenderingManager.add_action_frame(menu_manager.get_action_frame())
            clock.main_menu_window = menu_manager
