import pygame
from engine.system import Message, System

class EventSystem(System):

    def __init__(self, system):
        super().__init__("event", system)

    def init(self, game):
        pass

    def update(self, delta, game):
        messages = self.flush_messages()
        for message in messages:
            getattr(self, message.mtype)(game, *message.args)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.system.quit()
