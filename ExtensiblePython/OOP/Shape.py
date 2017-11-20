import math


class Shape2D:
    def area(self):
        raise NotImplementedError()


# inheritance + encapsulation
class Square(Shape2D):
    def area(self):
        return self.width ** 2

    def __init__(self, width):
        self.width = width


class Disk(Shape2D):
    def area(self):
        return math.pi * self.radius ** 2

    def __init__(self, radius):
        self.radius = radius

# object
shapes = [Square(2), Disk(3)]
for shape in shapes:
    print(shape.area())
