"""Defines the GameSystem class"""
import logging

import pygame

from engine.system import Message, System
from engine.game.classes.entity import Entity
from engine.game.primitive.vector import Vector

class GameSystem(System):

    def __init__(self, system):
        super().__init__("game", system)

    def init(self, entities):
        pass

    def update(self, delta, entities):
        """Game system also handles exiting of the game"""
        super().update(delta, entities)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.system.message("game", Message("quit"))

    """Message calls"""

    def message_create_entity(self, entities, name):
        if entities.get(name):
            logging.warning(
                "Entity with name '%s' already exists. Overwriting." % name)
        entities[name] = Entity(name, Vector(0, 0), self.system)

    def message_add_entity(self, entities, entity):
        if entities.get(entity.name):
            logging.warning(
                "Entity with name '%s' already exists. Overwriting." % name)
        entities[entity.name] = entity

    def message_quit(self, entities):
        self.system.quit()