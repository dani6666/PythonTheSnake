import copy
import random

import numpy

from Bot.NeuralNetworkData import NeuralNetworkData


class NeuralNetworkDataHelper:
    @staticmethod
    def generate_data():
        return NeuralNetworkData(numpy.random.rand(16, 12) - 0.5, numpy.random.rand(12, 12) - 0.5,
                                 (numpy.random.rand(12, 4) - 0.5) / 10)

    @staticmethod
    def crossover_data(first_data, second_data):
        result = NeuralNetworkData(numpy.zeros(16, 12), numpy.zeros(12, 12), numpy.zeros(12, 4))
        for i in range(16):
            cross_point = random.randrange(-1, 13)
            for j in range(12):
                if j < cross_point:
                    result.input_first[i][j] = first_data.input_first[i][j]
                else:
                    result.input_first[i][j] = second_data.input_first[i][j]

        for i in range(12):
            cross_point = random.randrange(-1, 9)
            for j in range(12):
                if j < cross_point:
                    result.first_second[i][j] = first_data.first_second[i][j]
                else:
                    result.first_second[i][j] = second_data.first_second[i][j]

        for i in range(12):
            cross_point = random.randrange(-1, 3)
            for j in range(4):
                if j < cross_point:
                    result.second_output[i][j] = first_data.second_output[i][j]
                else:
                    result.second_output[i][j] = second_data.second_output[i][j]

        return result

    @staticmethod
    def mutate_data(data_to_mutate):
        result = copy.deepcopy(data_to_mutate)
        for i in range(16):
            first_mutation = random.randrange(0, 9)
            for j in range(first_mutation, first_mutation + 3):
                result.input_first[i][j] += random.uniform(-1, 1)

        for i in range(12):
            first_mutation = random.randrange(0, 9)
            for j in range(first_mutation, first_mutation + 3):
                result.input_first[i][j] += random.uniform(-1, 1)

        for i in range(12):
            first_mutation = random.randrange(0, 2)
            for j in range(first_mutation, first_mutation + 2):
                result.input_first[i][j] += random.uniform(-1, 1) / 10
