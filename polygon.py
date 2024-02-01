# polygon.py

class Polygon():
    def __init__(self, edges, cradius):
        self._edges = edges
        self._cradius = cradius

    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, edges):
        self._edges = edges
    
    @property
    def cradius(self):
        return self._cradius
    
    @cradius.setter
    def cradius(self, cradius):
        self._cradius = cradius

    

    def __repr__(self) -> str:
        pass

    def __eq__(self, __value: object) -> bool:
        pass

    def __gt__():
        pass

