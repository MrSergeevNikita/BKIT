from lab_python_oop.geoFigure import geoFigure
from lab_python_oop.ColorFigure import ColorFigure
import math
class Circle (geoFigure):
    figure_type = "Круг"
    def __init__ (self, color, radius):
        self.radius = radius
        self.f_color = ColorFigure()
        self.f_color.color = color

    def square(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиуса {}  площадью {}.'.format(
            Circle.get_figure_type(),
            self.f_color.color,
            self.radius,
            self.square()
        )