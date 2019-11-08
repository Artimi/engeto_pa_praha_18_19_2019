# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']

# Delete names from candidates
candidates.remove('Bruno')

# Print remaining candidates
print('Bruno removed from candidates:', candidates)

# Repeat element
candidates = candidates + ['Agnes'] * 2

# Print repeating element in list candidates
print('Repetition of Agnes in candidate list:', candidates)

# Join lists
employees = employees + candidates

# Print joined lists
print('Joined candidates and employees:', employees)

# Index 2
print('On index 2 is:', employees[2])

# Find out last index and assign it to variable
last_index = len(employees) - 1

# Last index
print('On index', last_index, 'is:', employees[last_index])