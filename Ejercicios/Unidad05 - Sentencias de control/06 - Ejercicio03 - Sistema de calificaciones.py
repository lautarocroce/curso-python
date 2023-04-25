nota = int(input('Escribe tu nota (0/10): '))
mensaje = None
if 9 <= nota <= 10:
    mensaje = 'A'
elif nota == 8:
    mensaje = 'B'
elif nota == 7:
    mensaje = 'C'
elif nota == 6:
    mensaje = 'D'
elif 0 <= nota < 6:
    mensaje = 'F'
else:
    mensaje = 'Valor incorrecto'
print(f'Su nota {nota} equivale a {mensaje}')

