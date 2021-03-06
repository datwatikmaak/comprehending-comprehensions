# Write a function `sums_to_n` that takes an argument `n`, and returns all two-element tuples that sum to `n`.
#
# sums_to_n(5)
# [(0,5), (1,4), (2,3), (4,1), (5,0)]

def sum_to_n(n):
    result = [(x, y)
              for x in range(n + 1)
              for y in range(n + 1)
              if x + y == n
              ]

    print(result)


sum_to_n(5)
