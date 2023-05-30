import sys

def get_results(word):
    ascii_values = get_ascii(word)
    binary_values = get_binary(word)
    return {'ascii': ascii_values, 'binary': binary_values}

def get_ascii(word):
    valores_ascii = []
    for caracter in word:
        valores_ascii.append(ord(caracter))
    return valores_ascii

def get_binary(word):
    binary_values = []
    for character in word:
        binary_values.append(bin(ord(character))[2:])
    return binary_values

menu = 0
while menu != 1 and menu != 2:
    menu = int(input('Menu\n=====\n1. Character\n2. Word: '))

if menu == 1:
    character = input('Enter a character: ')
    word = character
    type = "character"
elif menu == 2:
    word = input('Enter a word: ')
    type = "word"
    character = word  # Using the entire word as the value of character

print('Results\n===========')

results = get_results(word)
print('The ASCII code of the {1} "{0}" is: {2}'.format(
    character, type, results['ascii']))
print('The binary code of "{0}" is: {1}'.format(
    character, results['binary']))
