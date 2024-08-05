import matplotlib.pyplot as plt
import pickle

class Point:

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def

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