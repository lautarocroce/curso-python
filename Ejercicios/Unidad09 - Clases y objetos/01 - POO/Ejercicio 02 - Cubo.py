class Cubo:
    def __init__(self, ancho, profundidad, alto):
        self.ancho = ancho
        self.profundidad = profundidad
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.profundidad * self.alto

ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
profundidad = int(input('Proporciona la profundidad: '))

cubo = Cubo(ancho, profundidad, alto)
print(f'Volumen cubo: {cubo.calcular_volumen()}')
