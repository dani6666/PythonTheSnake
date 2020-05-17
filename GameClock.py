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
        done = False

        while not done:
            game_ended = False
            while not game_ended:
                clock.tick(10)
                actions = self.frame_actions_manager.carry_frame_actions(self.game_manager.get_current_game_state())
                game_ended = self.game_manager.simulate_move(actions)
                RenderingManager.render()

            popup = self.game_manager.popup
            leaving_game = None

            while leaving_game is None:
                clock.tick(10)
                QuitHandler.check_quit()
                click = MouseActionProvider.get_click_position()
                if click:
                    leaving_game = popup.check_click(click)
                    if leaving_game == True:
                        RenderingManager.reset_action_frames()
                        done = True
                    elif leaving_game == False:
                        self.game_manager.reset()
                RenderingManager.render()
