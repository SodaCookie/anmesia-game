import pygame

from engine.system import Message, System

class RenderSystem(System):

    def __init__(self, system):
        super().__init__("render", system)

    def init(self, game):
        pass

    def update(self, delta, game):
        messages = self.flush_messages()
        for message in messages:
            getattr(self, message.mtype)(game, *message.args)

        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        for poly in game.terrain:
            pygame.draw.polygon(surface, (0, 255, 0), [(point.x, point.y) for point in poly.points], 1)

        pygame.draw.circle(surface, (0, 0, 255), (game.player.position.x, game.player.position.y), 10)

    def move(self, game, vector):
        game.player.position += vector