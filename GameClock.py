import pygame

from Model.Vector import Vector
from Rendering.RenderingManager import RenderingManager
from ActionProviders.MouseActionProvider import MouseActionProvider
from ActionProviders.QuitHandler import QuitHandler


class GameClock:

    def __init__(self, frame_actions_manager, game_manager):
        self.frame_actions_manager = frame_actions_manager
        self.game_manager = game_manager

    def start_game(self, is_bot_game, rendering_enabled):
        clock = pygame.time.Clock()
        end_reason = None
        done = False

        while not done:

            while not end_reason:
                if rendering_enabled:
                    clock.tick(10)
                actions = self.frame_actions_manager.carry_frame_actions(self.game_manager.get_current_game_state())
                end_reason = self.game_manager.simulate_move(actions)

            if not is_bot_game:
                self.game_manager.call_popup(end_reason)
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
                            end_reason = None
                            self.game_manager.reset()
                            popup_closed = True
                    RenderingManager.render()
            else:
                end_reason = None
                self.frame_actions_manager.pass_lost_game_info(self.game_manager.get_game_score())
                self.game_manager.reset()
