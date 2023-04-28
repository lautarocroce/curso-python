class PersonaNueva:
    #Agregarmos tuplas y diccionarios de términos en los atributos del objeto
    def __init__(self, nombre, apellido, edad):
        #Para encapsular los atributos se le pone un _ antes del nombre del atributo.
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #La idea es que se pueda acceder a los atributos con _ solo dentro de la clase. No desde afuera
    def mostrar_detalle(self):
        print(f'Objeto Persona 1: {self._nombre}, {self.apellido}, {self.edad}')

persona1 = PersonaNueva('Juan', 'Fernandez', 28)
persona1.mostrar_detalle()

