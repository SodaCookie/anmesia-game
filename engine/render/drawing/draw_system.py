import pygame

from engine.game.classes.shape import Shape
from engine.render.render_subsystem import RenderSubsystem

class DrawSystem(RenderSubsystem):

    def __init__(self, system):
        super().__init__("draw", system)

    def render(self, delta, entities, surface):
        # Get all terrain and lights
        for entity in entities.values():
            shapes = entity.get_components(Shape)
            for shape in shapes:
                polygon = shape.polygon + entity.position
                pygame.draw.polygon(surface, (0, 255, 0),
                    [(x, y) for x, y in polygon.points], 1)