def obtener_ascii(palabra):
    valores_ascii = []
    for caracter in palabra:
        valores_ascii.append(ord(caracter))
    return valores_ascii