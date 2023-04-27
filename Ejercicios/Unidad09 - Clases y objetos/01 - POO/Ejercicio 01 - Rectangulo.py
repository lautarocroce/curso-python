class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return print(f'Área del rectángulo: {self.base * self.altura}')

    def pedir_datos(self):
        base = int(input('Proporciona la base: '))
        altura = int(input('Proporciona la altura: '))

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
rectangulo = Rectangulo(altura, base)
rectangulo.calcular_area()
