import math
import os

import numpy

from Bot.BotTrainer import BotTrainer
from Bot.Move import Move
from Model.Vector import Vector


class BotManager:
    bot_resources_file_name = "saved-bot.json"

    def __init__(self):
        self.c = 0
        if os.path.exists(BotManager.bot_resources_file_name):
            file = open(BotManager.bot_resources_file_name)
            data = file.read()
            file.close()
        else:
            self.bot_trainer = BotTrainer()

    def perform_move(self, game_state):
        self.c += 1
        input_matrix = self.from_game_state_to_matrix(game_state)
        output_matrix = self.bot_trainer.perform_move(input_matrix)

        move = self.from_matrix_to_move(output_matrix)
        if self.c > 20:
            self.bot_trainer.game_lost()
            c = 0
        if move == 0:
            return [Vector(1, 0)]
        elif move == 1:
            return [Vector(-1, 0)]
        elif move == 2:
            return [Vector(0, 1)]
        elif move == 3:
            return [Vector(0, -1)]

    def game_lost(self):
        self.bot_trainer.game_lost()

    def from_game_state_to_matrix(self, game_state):
        return numpy.random.random((1, 16)) * 10

    def from_matrix_to_move(self, matrix):
        max = -math.inf
        for i in range(4):
            if max < matrix[0][i]:
                index = i
                max = matrix[0][i]

        return index
