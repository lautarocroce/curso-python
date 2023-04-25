"""
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *arg como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""

def multiplicar(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado

print(f'El resultado es {multiplicar(2,3,2)}')