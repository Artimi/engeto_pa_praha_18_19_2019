import string

message = 'abc def ghi jkl mno pqr stu vwx Yz'

alphabet = string.ascii_letters


def transform_letter(letter, delta):
    letter_code = alphabet.index(letter)
    new_code = (letter_code + delta) % len(alphabet)
    return alphabet[new_code]


def caesar(text, delta):
    result = ''
    for letter in text:
        if letter in string.ascii_letters:
            result += transform_letter(letter, delta)
        else:
            result += letter
    return result


print(caesar(message, 2))
print(caesar(message, -2))
