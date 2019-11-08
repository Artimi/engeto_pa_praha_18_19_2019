import pprint
import random

customers = [
    'Bettison, Elnora',
    'Doro, Jeffrey',
    'Idalia, Craig',
    'Conyard, Phil',
    'Skupinski, Wilbert',
    'McShee, Glenn',
    'Pate, Ashley',
    'Woodison, Annie'
]

products = [
    ('DROXIA', 33.86),
    ('WRINKLESS PLUS', 23.55),
    ('Claravis', 9.85),
    ('Nadolol', 12.35),
    ('Quinapril', 34.89),
    ('Doxycycline Hyclate', 23.43),
    ('Metolazone', 43.06),
    ('PAXIL', 14.78)
]

HEADER = ['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price']


def generate_row():
    name = random.choice(customers)
    item, unit_price = random.choice(products)
    amount = random.randint(1, 100)
    total_price = amount * unit_price
    return [name, item, amount, unit_price, total_price]


def generate_data(rows):
    assert rows >= 0, 'We can generate only positive number of rows.'
    result = [HEADER]
    for i in range(rows):
        result.append(generate_row())
    return result


pprint.pprint(generate_data(4))
