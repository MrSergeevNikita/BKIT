from abc import ABC, abstractmethod

class geoFigure(ABC):

    @abstractmethod
    def square(self):
        pass

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

