diaDescanso = input('¿Es dia de descanso? (S/N)')
diaVacaciones = input('¿Es dia de vacaciones? (S/N)')
if diaDescanso == "S":
    diaDescanso = True
else: diaDescanso = False
if diaVacaciones == "S":
    diaVacaciones = True
else: diaVacaciones = False
if diaDescanso or diaVacaciones:
    print('El padre puede ir al partido')
else:
    print('El padre no puede asistir al partido')