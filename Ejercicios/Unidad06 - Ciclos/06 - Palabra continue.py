#range() crea un conjunto de elementos que se le especifique

# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
        #el continue para la ejecución de la iteración en curso y ejecuta la siguiente iteración
    print(f'Valor: {i}')
