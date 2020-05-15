from Rendering.RenderPacket import RenderPacket
import copy

from Rendering.ResourceManager import ResourceManager


class DigitDisplay:

    def __init__(self, position, next_display=None, value=0):
        self.position = position
        self.value = value
        self.next_display = next_display

    def append_value(self):
        self.value += 1
        if self.value == 10:
            self.value = 0
            if self.next_display:
                self.next_display.append_value()

    def get_rendering_components(self):
        return [RenderPacket(ResourceManager.digits[self.value], copy.copy(self.position))]
