def divisores(n = 12):
    resultado = []
    for i in range(1, n + 1):
        if n % i == 0:
            resultado.append(i)
    return resultado 
divisores()