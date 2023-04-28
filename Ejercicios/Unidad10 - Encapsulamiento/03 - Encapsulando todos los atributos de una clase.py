class PersonaNueva:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @property
    def apellido(self):
        print('Llamando método get apellido')
        return self._apellido

    @property
    def edad(self):
        print('Llamando método get edad')
        return self._edad
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        print('Llamando método set apellido')
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        print('Llamando método set edad')
        self._edad = edad
    def mostrar_detalle(self):
        print(f'Objeto Persona: {self._nombre}, {self._apellido}, {self._edad}')

persona1 = PersonaNueva('Juan', 'Fernandez', 28)
persona1.mostrar_detalle()
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Croce'
persona1.edad = 30
persona1.mostrar_detalle()