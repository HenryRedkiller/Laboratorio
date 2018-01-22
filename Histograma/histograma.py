def calc_freq_letras(texto):
    """Regresa un diccionario con la frecuencia estadistica de cada letra"""

    dicc = {}

    for i in texto.replace(" ", ""):
        if i not in dicc:
            dicc[i] = 1
        else:
            dicc[i] += 1

    return dicc

