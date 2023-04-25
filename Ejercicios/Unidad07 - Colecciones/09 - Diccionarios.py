#El diccionario tiene una llave y un valor
#dict (key, value)
#Tampoco existe el índice en un diccionario. Para acceder a un
# elemento hay que usar la key que hemos puesto
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
#Acceder a un elemento (key)
print(diccionario['IDE'])
#otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#modificar elemento
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

#Recorrer los elementos de un diccionario
for elemento in diccionario:
    print(elemento)
    #Así imprimimos las llaves

#Para imprimir el contenido, no solo las llaves
for elemento, valor in diccionario.items():
    print(elemento,valor)

#Para imprimir solo las llaves
for elemento in diccionario.keys():
    print(elemento)

#Imprimir solo los valores
for valor in diccionario.values():
    print(valor)

#Comprobar existencia de algún elemento
print('IDE' in diccionario)

#Agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
#No se pueden agregar llaves duplicadas

diccionario.pop('DBMS')
print(diccionario)

#Limpiar diccionario sin eliminar variable
diccionario.clear()
print(diccionario)

#eiliminar la variable diccionario
del diccionario
print(diccionario) #Tira un error porque ya no se encuentra la variable