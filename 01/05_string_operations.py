# Save name
name = input('Name?')

# Print name
print(name)

# Save surname
surname = input('Surname?')

# Print surname
print(surname)

# Create and print variable full_name
full_name = name + ' ' + surname
print(full_name)

# Create and print variable name_length
name_length = len(full_name.replace('', ''))
print(name_length)

# Print bounded variable full_name
print('=' * name_length)
print(full_name)
print('=' * name_length)