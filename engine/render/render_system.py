from collections import OrderedDict

import pygame

from engine.render.lighting.lighting_system import LightingSystem
from engine.render.drawing.draw_system import DrawSystem

from engine.system import Message, System

class RenderSystem(System):

    def __init__(self, system):
        super().__init__("render", system)
        self.pipeline = OrderedDict()
        self.add_subsystem(LightingSystem(system))
        self.add_subsystem(DrawSystem(system))

    def add_subsystem(self, system):
        """Add another system to the render pipeline"""
        self.pipeline[system.name] = system

    def init(self, entities):
        for system in self.pipeline.values():
            system.init(entities)

    def quit(self, entities):
        for system in self.pipeline.values():
            system.quit(entities)

    def update(self, delta, entities):
        messages = self.flush_messages()
        for message in messages:
            message_call = message.mtype.split('.')
            # Passing messages to subsystems
            if len(message_call) == 2:
                self.pipeline[message_call[0]].message(Message(
                    message_call[1], *message.args))
            else:
                getattr(self, message.mtype)(game, *message.args)

        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))

        # Call systems
        for system in self.pipeline.values():
            system.render(delta, entities, surface)

        pygame.display.flip()