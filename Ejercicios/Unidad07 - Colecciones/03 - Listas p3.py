#Definir lista de tipo str
nombres = ['Juan','Carla','Ricardo','María']
#Imprimir la lista
print(nombres)
#Acceder a los elementos de manera individual en la lista
print(nombres[0])
print(nombres[2])
#Acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#Imprimir un rango
#Sin incluir el indice 2
print(nombres[0:2])
#Desde el inicio de la lista hasta el 3 sin incluirlo
print(nombres[:3])
#Desde el indice indicado hasta el final de la lista
print(nombres[1:])
#Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')
#Preguntar el largo de una lsita
print(len(nombres))
#Agregamos un elemento
nombres.append('Lorenzo')
print(nombres)
#Insertar un elemento en un índice especifico
nombres.insert(1, 'Octavio')
print(nombres)
#Eliminar un elemento por valor, no por índice
nombres.remove('Octavio')
print(nombres)
#Eliminar el último valor de la lista
nombres.pop()
print(nombres)
#eliminar por medio de un índice
del nombres[0]
print(nombres)
#Limpiar lista
nombres.clear()
print(nombres)
#Eliminar lista (no su contenido)
del nombres
print(nombres) #Sale un error porque ya no existe la lista que queremos imprimir