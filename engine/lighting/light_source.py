"""Defines the Source class"""
from pygame import Rect

class LightSource(object):
    """Represents the lighting object to handling lighting"""

    def __init__(self, vector, radius, strength=1):
        """Create a new light source with a location at a vector, with a
        radius and strength value (float between 0 and 1)."""
        self.vector = vector
        self.radius = radius
        self.strength = strength

    def move(self, vector):
        self.vector = vector

    def process(self, polygons, view):
        """Takes a list of polygons and will return a list of triangle to
        render to the screen based on the view"""
        points = polygon.points