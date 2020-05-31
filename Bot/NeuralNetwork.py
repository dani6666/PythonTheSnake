import numpy


class NeuralNetwork:

    def __init__(self, network_weights):
        # 16 x 12 x 12 x 4
        self.network_weights = network_weights

    def get_output(self, input_var):
        val = numpy.dot(input_var, self.network_weights.input_first)
        first_layer = self.sigmoid(val)
        second_layer = self.sigmoid(numpy.dot(first_layer, self.network_weights.first_second))

        return self.sigmoid(numpy.dot(second_layer, self.network_weights.second_output))

    @staticmethod
    def sigmoid(x):
        return x / (1 + numpy.exp(-x))
