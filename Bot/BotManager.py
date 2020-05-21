import os

from Bot.BotTrainer import BotTrainer


class BotManager:
    bot_resources_file_name = "saved-bot.json"
    def __init__(self):
        if os.path.exists(BotManager.bot_resources_file_name):
            file = open(BotManager.bot_resources_file_name)
            data = file.read()
            file.close()
        else:
            self.bot_trainer = BotTrainer()

    def perform_move(self, game_state):
        input_matrix = self.from_game_state_to_matrix(game_state)
        output_matrix = self.bot_trainer.perform_move(input_matrix)

        return self.from_matrix_to_move(output_matrix)

    def game_lost(self):
        self.bot_trainer.game_lost()

    def from_game_state_to_matrix(self, game_state):


    def from_matrix_to_move(self, matrix):
