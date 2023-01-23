from enum import Enum
from math import *


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class PointFactory:
    @staticmethod
    def new_cartesion_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = PointFactory(2, 3)
    p2 = PointFactory.new_polar_point(1, 2)
    print(p)
    print(p2)
