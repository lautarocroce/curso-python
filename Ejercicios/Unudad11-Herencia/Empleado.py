from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} \nSueldo: {self._sueldo}'


if __name__ == '__main__':
    empleado1 = Empleado('Juan', 28, 5000)
    print(empleado1.nombre)
    print(empleado1.edad)
    print(empleado1._sueldo)