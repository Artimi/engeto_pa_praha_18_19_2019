
credit_card_number = '49927398716'
numbers = [int(i) for i in credit_card_number]
# 1.	Reverse the digits	61789372994
reversed_numbers = list(reversed(numbers))
# 2.	Sum the odd digits	6 + 7 + 9 + 7 + 9 + 4 = 42 = s1
s1 = sum(reversed_numbers[::2])
print(s1)

# 3.	The even digits	1, 8, 3, 2, 9
even = reversed_numbers[1::2]
# 3a.	Each even digit x 2	2, 16, 6, 4, 18
even_double = [i * 2 for i in even]
# 3b.	Sum the digits of each multiplication	2, 7, 6, 4, 9
sum_digits = [
    sum([int(digit)for digit in str(i)])
    for i in even_double
]
# 3c.	Sum the the partial sums	2 + 7 + 6 + 4 + 9 = 28 = s2
s2 = sum(sum_digits)
print(s2)
# 4.	The sum s1+s2 ends with digit 0	s1 + s2 = 70
s = s1 + s2
# Output	The function returns value	True
print(s % 10 == 0)
