from Menu.Button import Button
from GameSettings import GameSettings
from Vector import Vector


class MainMenuWindow:

    def __init__(self):
        self.start_button = Button(Vector(0, 0), Vector(50, 50))

    def handle_mouse_click(self, click_position):
        if self.start_button.contains_posision(click_position):
            self.start_button.is_marked = True
            return True

    def get_game_settings(self):
        return GameSettings(False)
