"""Define Polygon class"""
from engine.game.primitive.vector import Vector
from engine.game.primitive.segment import Segment

class Polygon(object):

    def __init__(self, *points):
        """Creates a list of points"""
        self.points = points
        # Create segments
        self.segments = []
        for point1, point2 in zip(points, points[1:] + points[:1]):
            self.segments.append(Segment(point1, point2 - point1))

    def __add__(self, vector):
        new_points = [Vector(x + vector.x, y + vector.y) \
            for x, y in self.points]
        return Polygon(*new_points)

    def move(self, vector):
        """Moves the polygon in place by a given vector"""
        # Shift all points
        for point in self.points:
            point.x += vector.x
            point.y += vector.y

        # Shift all segments
        for segment in self.segments:
            segment.anchor.x += vector.x
            segment.anchor.y += vector.y