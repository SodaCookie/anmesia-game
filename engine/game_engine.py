"""Defines the Game object"""
from collections import OrderedDict

import pygame

class GameEngine(object):

    def __init__(self):
        super().__init__()
        self.systems = OrderedDict()
        self.entities = {}
        self.prevtime = 0
        self.running = True

    def add_system(self, system):
        self.systems[system.name] = system

    def run(self):
        """Run the game"""
        # Initiate pygame, screen, game object, clock
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()

        for system in self.systems:
            self.systems[system].init(self.entities)

        # Game loop
        while self.running:
            delta = pygame.time.get_ticks() - self.prevtime
            self.prevtime = pygame.time.get_ticks()
            for system in self.systems:
                self.systems[system].update(delta, self.entities)
            clock.tick(60)

        for system in self.systems:
            self.systems[system].quit(self.entities)

        pygame.quit()

    def message(self, system, message):
        """Sends a message to another system by name. Takes a system name
        as a string and the message object to pass."""
        self.systems[system].message(message)

    def quit(self):
        """Tells the system to quit on the next game loop"""
        self.running = False