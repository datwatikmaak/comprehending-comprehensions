# Ask the user to enter some integers, separated by spaces.  Sum the different numbers they enter.
numbers = input("Enter some integers, separated by spaces: ")

sum_of_numbers = sum({int(num)
                      for num in numbers.split()})

print(sum_of_numbers)
