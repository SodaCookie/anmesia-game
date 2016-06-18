"""Vector class to represent a 2 dimensional vector"""
import math

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalized(self):
        magnitude = self.get_magnitude()
        x = self.x / magnitude
        y = self.y / magnitude
        return Vector(x, y)

    def rotate(self, angle):
        x = math.cos(angle) * self.x - math.sin(angle) * self.y
        y = math.sin(angle) * self.x + math.cos(angle) * self.y
        return Vector(x, y)

    def angle(self, reference):
        return math.atan2(self.y, self.x) - \
            math.atan2(reference.y, reference.x)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def set_magnitude(self, new_magnitude):
        old_magnitude = self.get_magnitude()
        ratio = new_magnitude/old_magnitude
        self.x *= ratio
        self.y *= ratio

    """PROPERTIES"""

    magnitude = property(get_magnitude, set_magnitude)

    """CLASS METHODS"""

    @classmethod
    def up(self):
        return Vector(0, -1)

    @classmethod
    def down(self):
        return Vector(0, 1)

    @classmethod
    def right(self):
        return Vector(1, 0)

    @classmethod
    def left(self):
        return Vector(-1, 0)

    """DUNDER OVERRIDES"""

    """simple addition of vectors"""
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, number):
        x = self.x * number
        y = self.y * number
        return Vector(x, y)

    def __div__(self, number):
        x = self.x / number
        y = self.y / number
        return Vector(x, y)

    def __rmul__(self, number):
        return self * number

    def __lt__(self, other):
        return self.magnitude < other.magnitude

    def __le__(self, other):
        return self.magnitude <= other.magnitude

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x or self.y != other.y)

    def __gt__(self, other):
        return self.magnitude > other.magnitude

    def __ge__(self, other):
        return self.magnitude >= other.magnitude

    def __neg__(self):
        x = self.x * -1
        y = self.y * -1
        return Vector(x, y)

    def __str__(self):
        return "Vector(%f, %f)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()
