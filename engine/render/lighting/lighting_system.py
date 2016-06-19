import pygame

from engine.game.classes.lightsource import LightSource
from engine.game.classes.shape import Shape
from engine.render.render_subsystem import RenderSubsystem

class LightingSystem(RenderSubsystem):

    def __init__(self, system):
        super().__init__("lighting", system)

    def render(self, delta, entities, surface):
        # Get all terrain and lights
        lights = []
        terrain = []
        for entity in entities.values():
            lights.extend(entity.get_components(LightSource))
            terrain.extend(entity.get_components(Shape))

        # Filter ignore lighting
        terrain = [s.polygon for s in terrain if not s.ignore_lighting]

        lighting_triangles = []
        for light in lights:
            lighting_triangles.append((light.process(
                terrain, ((0, 0), surface.get_size())), light))

        buff = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        for triangles, light in lighting_triangles:
            for poly in triangles:
                pygame.draw.polygon(surface, (255*light.strength, 255*light.strength, 255*light.strength), [(point.x, point.y) for point in poly.points])