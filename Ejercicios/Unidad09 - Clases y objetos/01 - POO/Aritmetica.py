#Creamos la clase, sus atributos y sus métodos
class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return  self.operandoA * self.operandoB

    def dividir(self):
        return  self.operandoA / self.operandoB
#Creamos el objeto
aritmetica1 = Aritmetica(5,3)
print(f'La suma de {aritmetica1.operandoA} más {aritmetica1.operandoB} es igual a {aritmetica1.sumar()}')
print(f'La resta de {aritmetica1.operandoA} menos {aritmetica1.operandoB} es igual a {aritmetica1.restar()}')
print(f'La multiplicación de {aritmetica1.operandoA} por {aritmetica1.operandoB} es igual a {aritmetica1.multiplicar()}')
print(f'La división de {aritmetica1.operandoA} y {aritmetica1.operandoB} es igual a {aritmetica1.dividir()}')
