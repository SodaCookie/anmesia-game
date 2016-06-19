import pygame
from engine.system import Message, System

class EventSystem(System):

    def __init__(self, system):
        super().__init__("event", system)

    def init(self, game):
        pass

