"""Basic character class"""
from engine.game.physics_system import PhysicsSystem
import pygame

class Character(PhysicsSystem):
    def __init__(self, x, y):
        super().__init__()
        self.position = Vector(x, y)
        self.health = 100
        self.move_speed = 50

    def update(self, delta, game):
        self.handle_movement()
        super().update(delta, game)

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
          self.move(0, -self.move_speed)
        if keys[pygame.K_DOWN]:
          self.move(0, self.move_speed)
        if keys[pygame.K_RIGHT]:
          self.move(self.move_speed, 0)
        if keys[pygame.K_LEFT]:
          self.move(-self.move_speed, 0)
