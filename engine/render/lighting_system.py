import pygame
from engine.system import Message, System

class LightingSystem(System):

    def __init__(self, system):
        super().__init__("lighting", system)

    def init(self, game):
        pass

    def add_light(self, game, light):
        game.lights.append(light)

    def update(self, delta, game):
        messages = self.flush_messages()
        for message in messages:
            getattr(self, message.mtype)(game, *message.args)

        surface = pygame.display.get_surface()
        lighting_triangles = []
        for light in game.lights:
            lighting_triangles.append((light.process(
                game.terrain, ((0, 0), surface.get_size())), light))

        for triangles, light in lighting_triangles:
            for poly in triangles:
                pygame.draw.polygon(surface, (255*light.strength, 255*light.strength, 255*light.strength), [(point.x, point.y) for point in poly.points])