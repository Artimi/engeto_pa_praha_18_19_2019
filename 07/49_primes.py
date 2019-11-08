def list_primes(n):
    numbers = list(range(2, n + 1))
    result = []
    while numbers:
        i = numbers.pop(0)
        result.append(i)
        for num in numbers:
            if num % i == 0:
                numbers.remove(num)
    return result


def is_prime(number):
    if number <= 0:
        return False
    if number in (1, 2):
        return True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


print(list_primes(23))
