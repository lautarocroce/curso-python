class PersonaNueva:
    #Agregarmos tuplas y diccionarios de términos en los atributos del objeto
    def __init__(self, nombre, apellido, edad):
        #Para encapsular los atributos se le pone un _ antes del nombre del atributo.
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #Método get
    #Por medio del decorador @property no hace falta poner () para llamar al método
    #ej: antes: persona1._nombre() || ahora: persona1._nombre
    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre
    #La idea es que se pueda acceder a los atributos con _ solo dentro de la clase. No desde afuera

    #Definimos el setter
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre
    def mostrar_detalle(self):
        print(f'Objeto Persona 1: {self._nombre}, {self.apellido}, {self.edad}')

persona1 = PersonaNueva('Juan', 'Fernandez', 28)
print(persona1._nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
