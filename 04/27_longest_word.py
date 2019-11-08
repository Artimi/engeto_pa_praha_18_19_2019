words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

max_length = 0
max_word = None
while words:
    word = words.pop()
    word_len = len(word)
    if word_len > max_length:
        max_word = word
        max_length = word_len


print((max_word, max_length))


# another approach
words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

max_word = max(words, key=len)
print((max_word, len(max_word)))
