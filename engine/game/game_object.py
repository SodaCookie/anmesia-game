"""Defines the main game object that stores all state"""
from engine.game.player.player import Player

class GameObject(object):

    def __init__(self):
        self.player = None
        self.terrain = []
        self.lights = []