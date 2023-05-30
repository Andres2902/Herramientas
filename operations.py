def get_results(word):
    ascii_values = get_ascii(word)
    binary_values = get_binary(word)
    return {'ascii': ascii_values, 'binary': binary_values}
def obtener_ascii(palabra):
    valores_ascii = []
    for caracter in palabra:
        valores_ascii.append(ord(caracter))
    return valores_ascii
