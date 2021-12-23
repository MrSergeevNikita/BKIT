# Класс прямоугольник
from lab_python_oop.geoFigure import geoFigure
from lab_python_oop.ColorFigure import ColorFigure


class rectangle(geoFigure):
    figure_type = "прямоугольник"
# Класс должен содержать конструктор по параметрам «ширина», «высота» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета
    def __init__ (self, color, width, height):
        self.width = width
        self.height = height
        self.f_color = ColorFigure()
        self.f_color.color = color


    def square(self):
        return self.width * self.height


    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            rectangle.get_figure_type(),
            self.f_color.color,
            self.width,
            self.height,
            self.square()
        )