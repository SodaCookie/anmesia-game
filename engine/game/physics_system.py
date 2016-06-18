"""Object affected by physics"""
from engine.game.primitive.vector import Vector
from engine.system import System

class PhysicsSystem(System):
    def __init__(self):
        self.position = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.mass = 1

    def move(self, vector):
        self.position += vector

    def apply_force(self, vector):
        self.velocity += (vector / self.mass)

    def update(self, delta, game):
        self.handle_messages()
        self.handle_movement(delta)

    def handle_messages(self):
        messages = self.flush_messages()
        for message in messages:
            getattr(self, message.mtype)(message.args)

    def handle_movement(self, delta):
        seconds = delta / 1000
        real_velocity = self.velocity + self.acceleration * seconds
        real_position = self.position + self.velocity * seconds
