from InfoTracker.DigitDisplay import DigitDisplay
from Model.Vector import Vector


class ScoreTracker:

    def __init__(self, position, length):
        self.score = 0
        self.position = position
        self.length = length
        self.displays = [
            DigitDisplay(self.position + Vector(length - 1, 0)),
            DigitDisplay(self.position + Vector(length - 2, 0)),
            DigitDisplay(self.position + Vector(length - 3, 0))
        ]
        self.displays[0].next_display = self.displays[1]
        self.displays[1].next_display = self.displays[2]

    def increment_score(self):
        self.score += 1
        self.displays[0].increment_value()

    def reset(self):
        self.score = 0
        self.displays[0].reset()

    def get_rendering_components(self):
        return \
            self.displays[0].get_rendering_components() + \
            self.displays[1].get_rendering_components() + \
            self.displays[2].get_rendering_components()
