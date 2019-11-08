

sentence = 'a speech sound that is produced by comparatively open configuration of the vocal tract'
vowels = 'aeiouy'
consonants_count = 0
vowels_count = 0

for letter in sentence:
    if not letter.isalpha():
        continue
    if letter in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f'No. consonants: {consonants_count} | No. vowels: {vowels_count}')
