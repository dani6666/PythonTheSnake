class NeuralNetworkData:
    def __init__(self,input_first, first_second, second_third, third_output):
        self.input_first = input_first.T
        self.first_second = first_second.T
        self.second_third = second_third.T
        self.third_output = third_output.T
