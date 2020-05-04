class ActionFrame:

    def __init__(self, components=[], bg_color=(150, 150, 150)):
        self.components = components
        self.bg_color = bg_color

    def add_rendering_component(self, component):
        self.components.append(component)

    def remove_rendering_component(self, component):
        self.components.remove(component)

    def get_bg_color(self):
        return self.bg_color

    def get_rendering_components(self):
        return [rc for c in self.components for rc in c.get_rendering_components()]
