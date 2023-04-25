n = int(input('Ingrese un numero: '))
dentroRango = n >= 0 and n <= 5
if dentroRango:
    print(f'El numero {n} esta entre 0 y 5')
else:
    print(f'El numero {n} no esta entre 0 y 5')