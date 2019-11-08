COINS = [50, 20, 10, 5, 2, 1]


def coins(amount):
    result = {}
    for coin in COINS:
        if not amount:
            break
        quotient, remainder = divmod(amount, coin)
        if quotient:
            result[coin] = quotient
        amount = remainder
    return result


print(coins(124))
