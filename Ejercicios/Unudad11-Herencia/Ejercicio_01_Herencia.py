class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        print('Vehiculo'.center(20, '-'))
        return 'Color: ' + self._color + ' Ruedas: ' + str(self._ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return super().__str__() + ' Velocidad: ' + str(self._velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()}\nTipo: {self._tipo}'

vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)
coche = Coche('Azul', 4, 150)
print(coche)
bicicleta = Bicicleta('Naranja', 2, 'Urbana')
print(bicicleta)