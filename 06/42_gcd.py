

def gcd(a, b):
    while True:
        quotient, remainder = divmod(a, b)
        if remainder == 0:
            return b
        a, b = b, remainder


print(gcd(414, 78))
print(gcd(414, 49))
