# TODO: Given a list of integers, use a list comprehension to calculate the sum of the factorials of those integers.
#
# Stel dat de list is `[3, 4, 5]` dan is de oplossing van deze oefening:
#
# 3! = 3 \times 2 \times 1 = 6
# 4! = 4 \times 3 \times 2 \times 1 = 24
# 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
#
# Oplossing is dan: 6 + 24 + 120 = 150

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


nums = [3, 4, 5]

total = sum([factorial(num)
             for num in nums])

print(total)
