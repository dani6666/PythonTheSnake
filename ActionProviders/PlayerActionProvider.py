import pygame


class PlayerActionProvider:

    def __init__(self, input_sieves):
        self.input_sieves = input_sieves
        self.players = len(input_sieves)

    def retrieve_input(self, events):
        actions = []

        for i in range(self.players):
            actions.append(self.input_sieves[i].get_move(events))

        return actions
