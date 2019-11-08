repetitions = int(input('Enter the number of repetitions:'))
string = input('Enter the string:')

words = string.split(' ')
result = []
while words:
    word = words.pop(0)
    current_repetition = repetitions
    while current_repetition > 0:
        result.append(word)
        current_repetition -= 1

print(' '.join(result))
