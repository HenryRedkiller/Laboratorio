def calc_freq_letras(texto):
    """Regresa un diccionario con la frecuencia estadistica de cada letra"""

    dicc = {}

    for i in texto.lower().replace(" ", ""):
        if i not in dicc:
            dicc[i] = 1
        else:
            dicc[i] += 1

    return dicc


def convertir_llaves_a_lista(dicc):
    """Convierte las llaves del dicionario a una lista y las ordena"""

    return sorted(dicc.keys())
