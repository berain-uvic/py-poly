# polygon.py
import math


class Polygon():
    def __init__(self, n, R):
        self._n = n
        self._R = R

    @property
    def count_edges(self):
        return self._n
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        return 1 / 2 * self._n * self.side_length() * self.apothem()

    @property
    def perimeter(self):
        return self._n * self.side_length()

    def __repr__(self) -> str:
        return f'Polygon(n={self._n}, R={self._R})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Polygon):
            return (self._n, self._R) == (other._n, other._R)
        else:
            return False

    def __gt__(self, other) -> bool:
        if isinstance(other, Polygon):
            return self._n > other._n
        else:
            return False

