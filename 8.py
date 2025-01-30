def contar_vocales_consonantes(texto):
    conteo = {'vocales': 0, 'consonantes': 0}
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnñpqrtstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    for letra in texto:
        if letra in vocales:
            conteo['vocales'] += 1
        elif letra in consonantes:
            conteo['consonantes'] += 1
    return conteo
frase = "mañana tengo examen"
fin = contar_vocales_consonantes(frase)
print(fin)
