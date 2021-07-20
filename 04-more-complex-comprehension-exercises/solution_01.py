def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


numbers = range(1, 6)

print(sum([fact(one_number)
           for one_number in numbers]))
