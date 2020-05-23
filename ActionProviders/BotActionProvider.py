from Bot.BotManager import BotManager


class BotActionProvider:

    bool = True

    def __init__(self):
        self.move = None
        self.bot = BotManager()

    def retrieve_input(self):
        return self.move

    def start_thinking(self, game_state):
        self.move = self.bot.perform_move(game_state)

    def inform_about_lose(self):
        self.bot.game_lost()
