import random

ATTEMPTS = 10


def print_crossword(word, guessed):
    for letter in word:
        if letter in guessed:
            print(letter, end='')
        else:
            print('_', end='')
    print()


def hangman(words):
    word = random.choice(words)
    guessed = set()
    for attempt in range(ATTEMPTS, 0, -1):
        guess = input(f'Guess a letter ({attempt} guesses available): ')
        assert len(guess) == 1
        guessed.add(guess)
        print_crossword(word, guessed)
        if set(word).issubset(guessed):
            print('You win!')
            return
    print('You lose')


hangman(['Hangman', 'available', 'increase'])
