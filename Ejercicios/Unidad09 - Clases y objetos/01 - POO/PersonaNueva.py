class PersonaNueva:
    #Agregarmos tuplas y diccionarios de términos en los atributos del objeto
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Objeto Persona 1: {self.nombre}, {self.apellido}, {self.edad}, {self.valores}, {self.terminos}')

persona1 = PersonaNueva('Juan', 'Fernandez', 28, '456533562', 2, 3, 5, p='pera')
persona1.mostrar_detalle()

