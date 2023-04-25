#Dada la siguiente tupla
#Crea una lista que sólo incluya los números menores a 5

#Creamos la lista
lista = list()
#Creamos la tupla
tupla = (13,1,8,3,2,5,8)
#Iteramos la lista
for n in tupla:
    #Vamos llenando la lista con los valores menores o iguales a 5 de la tupla
    if n <= 5:
        lista.append(n)

#Ordenamos la lista
lista.sort()
print(lista)

