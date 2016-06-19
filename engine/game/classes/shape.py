from engine.game.classes.component import Component

from engine.game.primitive.polygon import Polygon

class Shape(Component):
    """Wrapper for a polygon"""

    def __init__(self, polygon, ignore_lighting=False):
        super().__init__()
        self.polygon = polygon
        self.ignore_lighting = ignore_lighting

    def set_ignore_lighting(self, ignore):
        self.ignore_lighting = ignore

    def __getattr__(self, name):
        return getattr(self.polygon, name)