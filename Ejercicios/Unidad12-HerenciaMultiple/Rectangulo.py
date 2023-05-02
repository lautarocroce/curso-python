from FiguraGeometrica import FiguraGeometrica
from Color import Color
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Rectangulo: Ancho = {self.ancho} Alto = {self.alto} Area = {self.area()}'