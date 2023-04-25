"""
Ejercicio: Calculadora de impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
Formula: pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
"""

def calculadoraImpuesto(pago,impuesto):
    return pago + pago * (impuesto/100)

print('Calculadora de impuesto:')
pago = int(input('Proporcione el pago sin impuesto: '))
impuesto = int(input('Proporcione el monto del impuesto: '))
print(f'Pago con impuestos: {calculadoraImpuesto(pago,impuesto)}')