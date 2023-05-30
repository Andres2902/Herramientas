def get_results(word):
    ascii_values = get_ascii(word)
    binary_values = get_binary(word)
    return {'ascii': ascii_values, 'binary': binary_values}
