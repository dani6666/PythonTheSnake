import pygame

from Model.Vector import Vector
from Rendering.RenderingManager import RenderingManager
from ActionProviders.MouseActionProvider import MouseActionProvider
from ActionProviders.QuitHandler import QuitHandler


class GameClock:

    def __init__(self, frame_actions_manager, game_manager, game_settings):
        self.frame_actions_manager = frame_actions_manager
        self.game_manager = game_manager
        self.game_settings = game_settings

    def start_game(self):
        clock = pygame.time.Clock()
        game_ended = False
        done = False

        while not done:

            while not game_ended:
                clock.tick(10)
                actions = self.frame_actions_manager.carry_frame_actions(self.game_manager.get_current_game_state())
                game_ended = self.game_manager.simulate_move(actions)
                RenderingManager.render()

            popup = self.game_manager.popup
            popup_closed = False

            while not popup_closed:
                clock.tick(10)
                QuitHandler.check_quit()
                click = MouseActionProvider.get_click_position()
                if click:
                    if popup.buttons[0].contains_position(click // Vector(40, 40)):
                        RenderingManager.reset_action_frames()
                        popup_closed = True
                        done = True
                    elif popup.buttons[1].contains_position(click // Vector(40, 40)):
                        game_ended = False
                        self.game_manager.reset()
                        popup_closed = True
                RenderingManager.render()
