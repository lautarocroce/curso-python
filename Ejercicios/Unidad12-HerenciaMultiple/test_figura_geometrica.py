from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
print('Creación objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(-5, 'rojo')
print(cuadrado1.__str__())
#MOR - Method Resolution Order
#Para saber en qué orden se ejecutan los métodos

#print(Cuadrado.mro())
print('Creación objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(5, 3, 'rojo')
print(rectangulo1.__str__())