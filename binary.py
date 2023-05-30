def get_binary(word):
    binary_values = []
    for character in word:
        binary_values.append(bin(ord(character))[2:])
    return binary_values