diaDescanso = input('¿Es dia de descanso? (S/N)')
diaVacaciones = input('¿Es dia de vacaciones? (S/N)')
if diaDescanso == "S":
    diaDescanso = True
else: diaDescanso = False
if diaVacaciones == "S":
    diaVacaciones = True
else: diaVacaciones = False
#Importante el uso de paréntesis para negar toda la sentencia.
if not (diaDescanso or diaVacaciones):
    print('El padre no puede asistir al partido')
else:
    print('El padre puede ir al partido')
print(diaDescanso)
print(diaVacaciones)
