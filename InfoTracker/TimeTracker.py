from InfoTracker.DigitDisplay import DigitDisplay
from Rendering.RenderPacket import RenderPacket
from Rendering.ResourceManager import ResourceManager
from Model.Vector import Vector
import time


class TimeTracker:

    def __init__(self, position):
        self.score = 0
        self.position = position
        self.displays = [
            DigitDisplay(self.position + Vector(3, 0)),
            DigitDisplay(self.position + Vector(2, 0), cap=6),
            DigitDisplay(self.position + Vector(0, 0))
        ]
        self.displays[0].next_display = self.displays[1]
        self.displays[1].next_display = self.displays[2]

        self.current_elapsed_time = 0
        self.registered_elapsed_time = 0
        self.start_time = time.time()

    def update_time(self):
        self.current_elapsed_time = time.time() - self.start_time
        delta_time = int(self.current_elapsed_time - self.registered_elapsed_time)
        if delta_time > 0:
            self.registered_elapsed_time = self.current_elapsed_time
            self.displays[0].add_value(delta_time)

    def reset(self):
        self.registered_elapsed_time = 0
        self.start_time = time.time()
        self.displays[0].reset()

    def unpause(self):
        self.start_time = time.time() - self.current_elapsed_time

    def get_rendering_components(self):
        return \
            [RenderPacket(ResourceManager.colon, self.position + Vector(1, 0))] + \
            self.displays[0].get_rendering_components() + \
            self.displays[1].get_rendering_components() + \
            self.displays[2].get_rendering_components()
