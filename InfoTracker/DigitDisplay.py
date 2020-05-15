from Rendering.RenderPacket import RenderPacket
import copy

from Rendering.ResourceManager import ResourceManager


class DigitDisplay:

    def __init__(self, position, cap=10, next_display=None, value=0):
        self.position = position
        self.cap = cap
        self.value = value
        self.next_display = next_display

    def increment_value(self):
        self.value += 1
        if self.value == self.cap:
            if self.next_display:
                self.next_display.increment_value()
            self.value = 0

    def add_value(self, value):
        self.value += value
        if self.value >= self.cap:
            if self.next_display:
                self.next_display.add_value(self.value // self.cap)
            self.value %= self.cap

    def reset(self):
        self.value = 0
        if self.next_display:
            self.next_display.reset()

    def get_rendering_components(self):
        return [RenderPacket(ResourceManager.digits[self.value], copy.copy(self.position))]
