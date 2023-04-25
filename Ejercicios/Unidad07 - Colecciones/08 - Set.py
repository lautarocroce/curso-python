# Coleccion set
# Set no mantiene un orden
# Set muestra los elementos de forma aleatoria
# Set no permite elementos duplicados
# Set no permite modificar los elementos
# Set permite agregar más elementos
# Set permite eliminar elementos
# Set no tiene índice

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento está presente en el set
print('Martes' in planetas) #arroja verdadero o falso
#agregar elementos
planetas.add('Tierra')
print(planetas)
#no soporta elementos duplicados
planetas.add('Tierra')
print(planetas)
#eliminar elementos
planetas.remove('Tierra') #tira error si el elemento no se encuentra
print(planetas)
#Eliminar elemento sin que tire error por no encontrar el elemento
planetas.discard('jupiters')
print(planetas)
#Limpiar set
planetas.clear()
print(planetas)
#Eliminar la coleccion set
del planetas
print(planetas)
