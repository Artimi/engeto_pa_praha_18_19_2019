

names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal'
        ]

sorted_names = []
for name in names:
    for i, sorted_name in enumerate(sorted_names):
        if name < sorted_name:
            sorted_names.insert(i, name)
            break
    else:
        sorted_names.append(name)

print(sorted_names)