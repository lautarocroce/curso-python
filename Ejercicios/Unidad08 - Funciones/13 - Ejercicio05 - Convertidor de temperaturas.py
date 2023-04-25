"""
Ejercicio: Convertidor de temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
(32 °F − 32) × 5/9 = 0 °C
(0 °C × 9/5) + 32 = 32 °F
"""

def celsiusFahrenheit(gradosC):
    return (gradosC * (9/5)) + 32

def fahrenheitCelsius(gradosF):
    return (gradosF - 32) * (5/9)

def mensaje():
    print('------------------')
    print('¿Qué desea hacer?')
    print('Fahrenheit a Celcius = 1')
    print('Celcius a Fahrenheit = 2')
    print('Salir = 0')

mensaje()
entrada = None
while entrada != 0:
    entrada = int(input())
    if entrada == 1:
        gradosF = float(input('Ingrese los grados Fahrenheit que desea convertir a grados Celcius: '))
        print(f'{gradosF} F° = {fahrenheitCelsius(gradosF):.2f} C°')
        mensaje()
    elif entrada == 2:
        gradosC = float(input('Ingrese los grados Celcius que desea convertir a grados Fahrenheit: '))
        print(f'{gradosC} C° = {celsiusFahrenheit(gradosC):.2f} F°')
        mensaje()
    elif entrada == 0:
        print('Adios')
    else:
        print('Ingresó una opción incorrecta. Vuelva a intentarlo')
        mensaje()
