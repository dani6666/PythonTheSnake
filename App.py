from GameInitializer import GameInitializer
from Menu.MainMenuWindow import MainMenuWindow
from MenuClock import MenuClock
from InputProviders.MouseInputProvider import MouseInputProvider
from Rendering.RenderingManager import RenderingManager
import pygame

from Rendering.ResourceManager import ResourceManager


class App:

    def start(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_mode((1, 1))
        ResourceManager.initialize_font()
        ResourceManager.convert_resources()
        input_provider = MouseInputProvider()
        menu_manager = MainMenuWindow()
        RenderingManager.add_action_frame(menu_manager.get_action_frame())
        game_intializer = GameInitializer()
        clock = MenuClock(input_provider, menu_manager, game_intializer)

        clock.start_app()
