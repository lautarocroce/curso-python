#Las tuplas son inmutables. Quiere decir que no se puede modificar, agregar o eliminar
#los datos agregados.

frutas = ('Naranja','Platano','Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a un rango
print(frutas[0:2]) #Sin incluir el último indice

#
#En las tuplas cuando se crea si sólamente tendrá un elemento
#hay que agregar una , después del elemento
#Ej: frutas('naranja',) Esa , debe ir sí o sí.
#En cambio cuando hay más de un elemento no es necesario
#agregar una , al final.
#

for fruta in frutas:
    print(fruta)
#Si queremos que la lista no salte de renglón
for fruta in frutas:
    print(fruta, end=' ')
print('')
#Para modificar los valores de una tupla hay que pasar la tupla
# a una lista, modificarla y luego volver a crear un  tupla

frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print(frutas)

#Eliminar la tupla por completo
del frutas
print(frutas) #Error porque no existe la tupla frutas

