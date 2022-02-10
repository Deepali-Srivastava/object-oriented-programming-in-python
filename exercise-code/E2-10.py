# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError('Radius should be positive')

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    def area(self):
        return 3.14 * self._radius * self._radius

c1 = Circle(7)
print( c1.radius, c1.diameter, c1.circumference, c1.area() )

