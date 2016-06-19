"""Defines the Component object"""

class Component(object):
    """Basic component object."""

    def __init__(self):
        self.entity = None

    def message(self, system, message):
        self.entity.system.message(system, message)