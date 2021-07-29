my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

joined_list = [one_item
               for sublist in my_list
               for one_item in sublist]

# joined_list = [one_item
#                for one_item in my_list]

print(joined_list)    # [10, 20, 30, 40, 50, 60, 70, 80, 90]

print([(x, y)
       for x in range(5)
       if not x % 2
       for y in range(5)
       if y % 2])

# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
