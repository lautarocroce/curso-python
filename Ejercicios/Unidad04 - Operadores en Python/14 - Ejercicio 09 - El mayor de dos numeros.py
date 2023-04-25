numero1 = int(input('Proporciona el número 1: '))
numero2 = int(input('Proporciona el número 2: '))
if numero1 < numero2:
    print('El número mayor es:',numero2)
elif numero1 > numero2:
    print('El número mayor es:',numero1)
else:
    print('Ambos números',numero1,'y',numero2,'son iguales')