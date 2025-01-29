def crear_diccionario():
    # Creamos un diccionario vacío
    diccionario = {}

    # Vamos a añadir claves y valores
    for i in range(1, 6):  # range(1, 6) da los números 1, 2, 3, 4, 5
        diccionario[i] = i ** 2  # Asignamos el cuadrado de i como valor

    return diccionario  # Devolvemos el diccionario con los resultados
# Llamamos a la función y mostramos el diccionario
resultado = crear_diccionario()
print(resultado)


