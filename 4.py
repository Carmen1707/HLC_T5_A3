def suma_promedio ():
    numeros = [1,2,3,4,5]
    suma = 0

    for i in numeros:
        suma = suma + i 

        print("La suma es" ,suma)
        print("El promedio es" ,suma/len(numeros))

suma_promedio()