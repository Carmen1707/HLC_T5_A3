def crear_diccionario(palabras):
    diccionario = {} #diccionario vacio 
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario
lista = ['gato', 'perro', 'elefante', 'botella']
fin = crear_diccionario(lista)
print (fin)
