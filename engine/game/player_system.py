import pygame

from engine.system import Message, System
from engine.game.player.player import Player
from engine.game.primitive.vector import Vector
from engine.game.primitive.polygon import Polygon
from engine.render.lighting.light_source import LightSource

class PlayerSystem(System):

    def __init__(self, system):
        super().__init__("player", system)

    def init(self, game):
        game.player = Player(Vector(640, 360))
        self.system.message("lighting", Message("add_light",
            LightSource(Vector(640, 360), 10)))
        game.terrain.append(Polygon(Vector(400, 400), Vector(450, 450), Vector(500, 420)))
        game.terrain.append(Polygon(Vector(10, 10), Vector(200, 200), Vector(0, 300)))
        # game.terrain.append(Polygon(Vector(400, 400), Vector(450, 450), Vector(500, 420)))

    def update(self, delta, game):
        messages = self.flush_messages()
        for message in messages:
            getattr(self, message.mtype)(game, *message.args)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.system.message("player", Message("move", Vector.up()))
        elif keys[pygame.K_a]:
            self.system.message("player", Message("move", Vector.left()))
        elif keys[pygame.K_s]:
            self.system.message("player", Message("move", Vector.down()))
        elif keys[pygame.K_d]:
            self.system.message("player", Message("move", Vector.right()))

    def move(self, game, vector):
        game.player.position += vector
        game.lights[0].position += vector