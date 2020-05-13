from Rendering.ActionFrame import ActionFrame
from Menu.Button import Button
from Model.GameSettings import GameSettings
from Model.Vector import Vector


class MainMenuWindow:

    def __init__(self):
        self.node_size = Vector(30, 30)
        self.start_button = Button(Vector(4, 13), Vector(3, 1), False)

    def handle_mouse_click(self, click_position):
        click_position = click_position.divide(self.node_size)
        if self.start_button.contains_posision(click_position):
            self.start_button.is_marked = True
            return True

    def get_game_settings(self):
        return GameSettings(False)

    def get_action_frame(self):
        return ActionFrame([Button], Vector(11, 15), self.node_size, [self.start_button])
