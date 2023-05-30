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