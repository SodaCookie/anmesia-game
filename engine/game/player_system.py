import pygame

from engine.system import Message, System
from engine.game.primitive.vector import Vector
from engine.game.primitive.polygon import Polygon
from engine.game.classes.entity import Entity
from engine.game.classes.lightsource import LightSource
from engine.game.classes.shape import Shape

class PlayerSystem(System):

    def __init__(self, system):
        super().__init__("player", system)
        self.player = None
        self.speed = 0.5

    def init(self, entities):
        self.player = Entity("Player", Vector(100, 100), self.system)
        self.player.add_component(Shape(Polygon(Vector(-5, -5), Vector(5, -5), Vector(5, 5), Vector(-5, 5)), True))
        # self.player.add_component(LightSource(Vector(0, 2), 100, 0.5))
        # self.player.add_component(LightSource(Vector(2, 0), 100, 0.5))
        # self.player.add_component(LightSource(Vector(0, -2), 100, 0.5))
        # self.player.add_component(LightSource(Vector(-2, 0), 100, 0.5))
        self.player.add_component(LightSource(Vector(0, 0), 100, 1))
        self.system.message("game", Message("add_entity", self.player))


        terrain = Entity("terrain", Vector(0, 0), self.system)
        terrain.add_component(Shape(Polygon(Vector(400, 400), Vector(450, 450), Vector(500, 420))))
        terrain.add_component(Shape(Polygon(Vector(10, 10), Vector(200, 200), Vector(0, 300))))
        self.system.message("game", Message("add_entity", terrain))
        # game.terrain.append()
        # game.terrain.append()

    def update(self, delta, entities):
        super().update(delta, entities)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.system.message("player", Message("move", Vector.up()*self.speed*delta))
        elif keys[pygame.K_a]:
            self.system.message("player", Message("move", Vector.left()*self.speed*delta))
        elif keys[pygame.K_s]:
            self.system.message("player", Message("move", Vector.down()*self.speed*delta))
        elif keys[pygame.K_d]:
            self.system.message("player", Message("move", Vector.right()*self.speed*delta))

    def message_move(self, game, vector):
        self.player.position += vector