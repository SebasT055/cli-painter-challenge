import math
import matplotlib.pyplot as plt
import pickle

class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y



class Circle:

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self):
        area_circulo = math.pi * (self.radius**2)
        return area_circulo

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return Circle with center at (x, y) and radius r




class Triangle:
    pass

class Rectangle:
    pass




class Painter:

FILE = ".painter"

def __init__(self) -> None:
    self.shapes: list = []
    self._load()

def _load(self) -> None:
    try:
        with open(Painter.FILE, "rb") as f:
            self.shapes = pickle.load(f)
    except (EOFError, FileNotFoundError):
        self.shapes = []

def _save(self) -> None:
    with open(Painter.FILE, "wb") as f:
        pickle.dump(self.shapes, f)

def add_shape(self, shape) -> None:
    self.shapes.append(shape)
    self._save()

def total_area(self) -> float:
    return sum(shape.area() for shape in self.shapes)

def clear(self) -> None:
    self.shapes = []
    self._save()