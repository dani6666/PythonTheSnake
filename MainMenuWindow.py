from Button import Button
from GameSettings import GameSettings
from Vector import Vector


class MainMenuWindow:

    def __init__(self):
        self.start_button = Button(Vector(0,0), Vector(0,0))

    def handle_mouse_click(self, click_position):


    def get_game_settings(self):
        return GameSettings(False)
