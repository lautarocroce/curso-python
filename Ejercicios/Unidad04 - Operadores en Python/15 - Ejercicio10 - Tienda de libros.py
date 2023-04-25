print('Proporcione los siguientes datos del libro:')
nombre = input('Proporciona el nombre: ')
ID = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: '))
envio = input('Indica si el envio es gratuito o no (True/False: ')
if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir True/ False'
"""
print('Nombre:',nombre)
print('ID:',ID)
print('Precio:',precio)
print('¿Envio gratuito?:',envio)
"""
print(f'''
    Nombre: {nombre}
    ID: {ID}
    Precio: {precio}
    ¿Envio gratuito?: {envio} 
''')