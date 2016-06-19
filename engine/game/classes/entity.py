"""Defines the Entity class"""

class Entity(object):

    def __init__(self, name, position, system):
        self.name = name
        self.position = position
        self.system = system
        self.components = []
        self.type_counts = {}

    def add_component(self, component):
        """Adds a component to this entity"""
        component.entity = self
        if type(component).__name__ not in self.type_counts:
            self.type_counts[type(component).__name__] = 0
        self.type_counts[type(component).__name__] += 1
        self.components.append(component)

    def remove_component(self, component):
        """Removes a component for the entity"""
        self.components.remove(component)
        self.type_counts[type(component).__name__] -= 1

    def get_components(self, ctype):
        """Returns a list of components of type ctype"""
        return [c for c in self.components if c.__class__ == ctype]

    def has_type(self, ctype):
        """Returns as an integer if the entity holds the given component"""
        return self.type_counts.get(ctype.__name__, 0)