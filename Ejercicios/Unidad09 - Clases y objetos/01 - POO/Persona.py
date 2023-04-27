#Se crea la clase
class Persona:
    #Se crea un método
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Objeto Persona 1: {self.nombre}, {self.apellido}, {self.edad}')


#Se crea un objeto de la clase persona y se imprime sus atributos.
persona1 = Persona('Juan', 'Fernandez', 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#Modificamos los valores del objeto
persona1.nombre = 'Lautaro'
persona1.apellido = 'Croce'
persona1.edad = 30
print(f'Objeto Persona 1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')

#Creamos y mostramos otro objeto
persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona 2: {persona2.nombre}, {persona2.apellido}, {persona2.edad}')

#Llamamos al método mostrar detalle
persona1.mostrar_detalle()

#Llamamos al método por medio de la clase
Persona.mostrar_detalle(persona1)

#En python se pueden agregar atributos a un objeto directamente pero no se agrega a la clase
persona1.telefono = '553554651'
print(persona1.telefono)
#Ese atributo teléfono no lo tendrá el objeto persona2 porque no telefono no lo tiene la clase Persona


