from unidecode import unidecode

def sanitizar(texto):
    return unidecode(texto.lower())