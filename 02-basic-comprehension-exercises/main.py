# take mylist = [10, 20, 30] and join it together with "*" characters
mylist = [10, 20, 30]
list_string = list(map(str, mylist))
# print(list_string)
joined_string = "*".join(list_string)
# print(joined_string)


# ask the user to enter multiple hex numbers (digits 0-9, and a-f), separated by whitespace, and sum those numbers
# 1234 ab56 ffe4
hex_numbers = input("Please enter multiple hex number: ")
list_of_hex_numbers = hex_numbers.split()


# ask the user to enter words separated with whitespace. show the number of non-whitespace characters in their input.
# this is a test = 11 characters
