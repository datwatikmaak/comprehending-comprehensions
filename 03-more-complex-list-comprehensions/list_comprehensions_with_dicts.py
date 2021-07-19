d = {"a": 1, "b": 2, "c": 3}

# key_of_d = [one_item
#             for one_item in d]
#
# print(key_of_d)
#
# value_of_d = [d[one_item] * 5
#               for one_item in d]
#
# print(value_of_d)

# tuple_of_d = [(one_item, d[one_item] * 5)
#               for one_item in d]
#
# print(tuple_of_d)

k = [key * d[key]
     for key in d]

print(k)
