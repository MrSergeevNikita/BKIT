from lab_python_oop.rectangle import rectangle
# Класс квардрат
class Square(rectangle):
    figure_type = "Квадрат"
    def __init__(self, color, side):
        super().__init__(color, side, side)
    def __repr__(self):
        return f"{Square.get_figure_type()} {self.f_color.color} цвета со стороной"\
               f" {self.width} и площадью {self.square()}"