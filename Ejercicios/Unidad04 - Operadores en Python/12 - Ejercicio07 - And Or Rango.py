edad = int(input('Introduce tu edad: '))
veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40
if veintes or treintas:
    #Para usar ' como parte del texto y encerrar el texto entre ' podemos usar \ antes de la ' que querramos que
    #esté incluida en el texto. ( \ = alt+92)
    if veintes:
        print('Dentro de los 20\'')
    else:
        print('Dentro de los 30\'')
else:
    #Para usar ' como parte del texto podemos encerrar el texto entre " texto "
    print("No está entre el rango de los 20' y 30'")