variable = int(input("¿Cómo estuvo tu día? (1 al 10): "))
if 0 < variable < 11:
    print("Mi día estuvo de:", variable)
    print("Adios.")
else:
    print("Su respuesta no fue la esperada. Adios.")
