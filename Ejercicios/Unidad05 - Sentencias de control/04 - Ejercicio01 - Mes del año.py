mes = int(input('Ingrese un mes del año (1/12): '))
if mes == 12 or 1 <= mes <3:
    print(f'El mes {mes} corresponde al verano.')
elif 3 <= mes < 6:
    print(f'El mes {mes} corresponde al otoño')
elif 6 <= mes < 9:
    print(f'El mes {mes} corresponde al invierno')
elif 9 <= mes < 12:
    print(f'El mes {mes} corresponde a la primavera')
else:
    print(f'El valor ingresado {mes} no es correcto')