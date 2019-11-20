import re

SYMBOLS = {
    # double
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4,
    # one
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}


def get_value(pair):
    return pair[1]


SYMBOLS_VALUE_SORTED = dict(sorted(SYMBOLS.items(), key=get_value, reverse=True))


def to_roman(arab):
    result = ''
    for symbol, value in SYMBOLS_VALUE_SORTED.items():
        count = arab // value
        arab = arab % value
        result += symbol * count
    return result


def to_arab(roman):
    result = 0
    for symbol, value in SYMBOLS.items():
        count = len(re.findall(symbol, roman))
        if count:
            roman = roman.replace(symbol, '')
        result += count * value
    return result


print(to_arab('MMMCMXCIX'))
print(to_roman(3999))
