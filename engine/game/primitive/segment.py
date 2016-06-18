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
        if other.direction.normalized() == self.direction.normalized():
            return None
        elif -other.direction.normalized() == self.direction.normalized():
            return None

        # Test intersection
        px1, dx1 = self.anchor.x, self.direction.x
        px2, dx2 = other.anchor.x, other.direction.x
        py1, dy1 = self.anchor.y, self.direction.y
        py2, dy2 = other.anchor.y, other.direction.y

        t2 = (dx1*(py2-py1) + dy1*(px1-px2)) / (dx2*dy1 - dy2*dx1)
        t1 = (px2+dx2*t2-px1) / dx1

        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            return Vector(px1 + dx1 * t1, py1 + dy1 * t1)
        return None

    def intersect_ray(self, ray):
        """Takes another segment object to represent as a ray and determine if this segment is intersecting the cast ray"""

        # Test if parallel
        if ray.direction.normalized() == self.direction.normalized():
            return None
        elif -ray.direction.normalized() == self.direction.normalized():
            return None

        # Test intersection
        px1, dx1 = ray.anchor.x, ray.direction.x
        px2, dx2 = self.anchor.x, self.direction.x
        py1, dy1 = ray.anchor.y, ray.direction.y
        py2, dy2 = self.anchor.y, self.direction.y

        try:
            t2 = (dx1*(py2-py1) + dy1*(px1-px2)) / (dx2*dy1 - dy2*dx1)
        except ZeroDivisionError:
            t2 = (dx1*(py2-py1) + dy1*(px1-px2)) / 0.00000001

        try:
            t1 = (px2+dx2*t2-px1) / dx1
        except ZeroDivisionError:
            t1 = (py2+dy2*t2-py1) / dy1

        if 0 <= t1 and 0 <= t2 <= 1:
            return Vector(px1 + dx1 * t1, py1 + dy1 * t1)
        return None

    def __str__(self):
        return "Segment(%s, %s)" % (str(self.anchor), str(self.direction))

    def __repr__(self):
        return self.__str__()
