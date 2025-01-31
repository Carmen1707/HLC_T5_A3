def divisores(n):
    resultado = []
    for i in range(1, n + 1):
        if n % i == 0:
            resultado.append(i)
    return resultado 
FIN = divisores(12)
print(FIN)