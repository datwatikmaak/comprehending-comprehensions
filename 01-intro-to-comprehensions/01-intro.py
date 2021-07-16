numbers = list(range(10))
print(numbers)


# make a new list with the square of the numbers list
output = []
for num in numbers:
    output.append(num * num)

print(output)


# the above code written as a list comprehension
output = [num * num for num in numbers]
print(output)


# the list comprehension in more readable way
output = [num * num
          for num in numbers]
print(output)


# capitalize words from a string of words
words = "This is a bunch of words".split()
output = [word.capitalize()
          for word in words]
print(output)
