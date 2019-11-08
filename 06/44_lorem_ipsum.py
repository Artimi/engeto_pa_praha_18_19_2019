import random

articles = ['the', 'a', 'an']
determiners = ['another', 'this', 'every', 'many']
subjects = ['cat', 'dog', 'man', 'woman']
verbs = ['sang', 'ran', 'jumped']
adverbs = ['loudly', 'quietly', 'well', 'badly']

orders = [
    [articles, subjects, verbs, adverbs],
    [determiners, subjects, verbs],
    [determiners, subjects, verbs, adverbs],
]


def generate_sentence():
    order = random.choice(orders)
    return ' '.join([random.choice(words) for words in order])


def generate_text(rows):
    return '\n'.join([generate_sentence() for _ in range(rows)])


print(generate_text(5))
