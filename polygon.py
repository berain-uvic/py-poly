# polygon.py
import math


class Polygon():
    def __init__(self, edges: int, cradius: float):
        self._edges = None
        self._cradius = None

        self.edges = edges
        self.cradius = cradius

    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, edges):
        if edges < 3:
            raise ValueError('Must be at least three edges/vertices.')
        self._edges = edges
    
    @property
    def cradius(self):
        return self._cradius
    
    @cradius.setter
    def cradius(self, cradius):
        if cradius <= 0:
            raise ValueError('Circumradius must be greater than zero.')
        self._cradius = cradius

    def iangle(self):
        return (self.edges - 2) * (180 / self.edges)

    def edge_length(self):
        return 2 * self.cradius * math.sin(math.pi / self.edges)

    def apothem(self):
        return self.cradius * math.cos(math.pi / self.edges)

    def area(self):
        return (1 / 2) * self.edges * self.edge_length() * self.apothem()

    def perimeter(self):
        return self.edges * self.edge_length()

    def __repr__(self) -> str:
        pass

    def __eq__(self, __value: object) -> bool:
        pass

    def __gt__():
        pass

