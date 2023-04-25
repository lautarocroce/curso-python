"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y debe regresar como resultado la suma de todos los valores pasados como argumentos.
"""

def sumar(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado

print(f'El resultado es {sumar(2,2,1,5)}')