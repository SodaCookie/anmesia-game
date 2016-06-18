"""Defines the Segment class"""
from engine.game.primitive.vector import Vector

class Segment(object):
    """Represents a segment"""

    def __init__(self, anchor, direction):
        self.anchor = anchor
        self.direction = direction

    def set_anchor(self, anchor):
        self.anchor = anchor

    def set_direction(self, direction):
        self.direction = direction

    def intersect(self, other):
        """Takes another segment object and determines if the segment is
        intersecting this segment"""

        # Test if parallel
        if other.direction.normalize() == self.direction.normalize():
            return False
        elif -other.direction.normalize() == self.direction.normalize():
            return False

        # Test intersection
        px1, dx1 = self.anchor.x, self.direction.x
        px2, dx2 = other.anchor.x, other.direction.x
        py1, dy1 = self.anchor.y, self.direction.y
        py2, dy2 = other.anchor.y, other.direction.y

        t2 = (dx1*(py2-py1) + dy1*(px1-px2)) / (dx2*dy1 - dy2*dx1)
        t1 = (px2+dx2*t2-px1) / dx1

        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            return True
        return False

    def intersect_ray(self, ray):
        """Takes another segment object to represent as a ray and determine if this segment is intersecting the cast ray"""

        # Test if parallel
        if other.direction.normalize() == self.direction.normalize():
            return False
        elif -other.direction.normalize() == self.direction.normalize():
            return False

        # Test intersection
        px1, dx1 = ray.anchor.x, ray.direction.x
        px2, dx2 = self.anchor.x, self.direction.x
        py1, dy1 = ray.anchor.y, ray.direction.y
        py2, dy2 = self.anchor.y, self.direction.y

        t2 = (dx1*(py2-py1) + dy1*(px1-px2)) / (dx2*dy1 - dy2*dx1)
        t1 = (px2+dx2*t2-px1) / dx1

        if 0 <= t1 and 0 <= t2 <= 1:
            return True
        return False