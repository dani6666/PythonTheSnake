from Model.Vector import Vector


class BotActionProvider:

    bool = True

    def __init__(self):
        self.move = None

    def retrieve_input(self):
        return self.move

    def start_thinking(self, game_state):
        if BotActionProvider.bool:
            self.move = Vector(0, 1)
        else:
            self.move = Vector(1, 0)

        BotActionProvider.bool = not BotActionProvider.bool
