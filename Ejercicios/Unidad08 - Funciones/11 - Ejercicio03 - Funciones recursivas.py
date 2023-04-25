"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5 debe imprimir:
5 4 3 2 1
En caso de pasar el valor 3, debe imprimir:
3 2 1
si se pasan valores negativos no imprime nada.
"""

def descendente(numero):
    if numero > 0:
        print(numero)
        return descendente(numero-1)
    elif numero == 0:
        return
    elif numero < 0:
        print('Valor incorrecto...')



descendente(5)