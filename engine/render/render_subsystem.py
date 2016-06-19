import pygame
from engine.system import Message, System

class RenderSubsystem(System):

    def __init__(self, name, system):
        super().__init__(name, system)

    def init(self, game):
        pass

    def update(self, delta, entities, surface):
        super().update(delta, entities)
        self.render()

    def render(self, delta, entities, surface):
        """Override. Called on every render system update"""
        pass