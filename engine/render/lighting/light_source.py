"""Defines the Source class"""
from itertools import chain

from pygame import Rect

from engine.game.primitive.vector import Vector
from engine.game.primitive.segment import Segment
from engine.game.primitive.polygon import Polygon

class LightSource(object):
    """Represents the lighting object to handling lighting"""

    def __init__(self, position, radius, strength=1):
        """Create a new light source with a location at a vector, with a
        radius and strength value (float between 0 and 1)."""
        self.position = position
        self.radius = radius
        self.strength = strength

    def move(self, position):
        self.position = position

    def process(self, polygons, view):
        """Takes a list of polygons and will return a list of triangle to
        render to the screen based on the view"""
        view = Rect(view)

        # Add view points and segments
        points = [Vector(*view.topleft), Vector(*view.bottomleft),
                  Vector(*view.bottomright), Vector(*view.topright)]
        segments = []
        for point1, point2 in zip(points, points[1:] + points[:1]):
            segments.append(Segment(point1, point2 - point1))

        # Add current points and segments
        for polygon in polygons:
            points.extend(polygon.points)
            segments.extend(polygon.segments)

        # Create rays to test
        rays = []
        for point in points:
            direction = point - self.position
            ray_left = Segment(self.position, direction.rotate(-0.00001))
            ray = Segment(self.position, direction)
            ray_right = Segment(self.position, direction.rotate(0.00001))
            rays.append(ray_left)
            rays.append(ray)
            rays.append(ray_right)

        # Test all intersections
        intersections = []
        for ray in rays:
            closest_intersection = None
            closest_magnitude = 2**32 - 1
            for segment in segments:
                intersect = segment.intersect_ray(ray)
                if intersect:
                    distance = intersect - self.position
                    if closest_intersection is None or \
                            distance.magnitude <= closest_magnitude:
                        closest_intersection = distance
                        closest_magnitude = distance.magnitude
            if closest_intersection:
                intersections.append(closest_intersection)

        # Sort intersects by angle
        right = Vector.right()
        intersections.sort(key=lambda point: point.angle(right))

        # Calculate light blocks
        blocks = []
        for i in range(len(intersections)):
            blocks.append(Polygon(self.position,
                intersections[i] + self.position,
                intersections[(i+1)%len(intersections)] + self.position))

        return blocks