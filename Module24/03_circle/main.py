import  math


class Circle:
    def __init__(self, coordinates_center = (0, 0), radius = 1):
        self.coordinates_center = coordinates_center
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def circumference_length(self):
        return  2 * math.pi * self.radius

    def height(self, k):
        self.radius *= k

    def intersection_with_circle(self, radius, coordinates_center = tuple()):
        if math.sqrt((self.coordinates_center[0] - coordinates_center[0]) ** 2 + (self.coordinates_center[1] - coordinates_center[1]) ** 2) < self.radius + radius:
            return True
        return False