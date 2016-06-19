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

    def collidepoint(self, vector):
        """Determines if a point is within a vector"""
        x, y = vector
        horizontal_line = Segment(Vector(0, y), Vector.right())
        points = []
        for segment in self.segments:
            intersect = segment.intersect_line(horizontal_line)
            if intersect:
                points.append(intersect)

        left = 0
        for intersect_x, intersect_y in points:
            if intersect_x < x:
                left += 1

        return left % 2

    def colliderangex(self, y):
        """Given a y value, returns a list of tuples representing x ranges
        that are found within the polygon at that y."""
        horizontal_line = Segment(Vector(0, y), Vector.right())
        points = []
        for segment in self.segments:
            intersect = segment.intersect_line(horizontal_line)
            if intersect:
                points.append(intersect)

        i = iter(sorted(points, key=lambda point: point.x))
        return [(first.x, second.x) for first, second in zip(i, i)]