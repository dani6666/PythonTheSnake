from Rendering.RenderPacket import RenderPacket
from Rendering.ResourceManager import ResourceManager


class InfoTracker:

    def __init__(self, position, score_tracker, time_tracker):
        self.position = position
        self.score_tracker = score_tracker
        self.time_tracker = time_tracker

    @property
    def score(self):
        return self.score_tracker.score

    @property
    def registered_elapsed_time(self):
        return self.time_tracker.registered_elapsed_time

    def increment_score(self):
        self.score_tracker.increment_score()

    def update_time(self):
        self.time_tracker.update_time()

    def reset(self):
        self.score_tracker.reset()
        self.time_tracker.reset()

    def unpause(self):
        self.time_tracker.unpause()

    def get_rendering_components(self):
        return [RenderPacket(ResourceManager.info_bar, self.position)] + \
            self.time_tracker.get_rendering_components() + self.score_tracker.get_rendering_components()
