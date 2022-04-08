"""
Creates the class Sphere, with a radius.
Includes functions to get radius,
and to calculate surface area and volume.
"""

from math import pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * pi * self.radius**2

    def volume(self):
        return (4/3) * pi * self.radius**3
