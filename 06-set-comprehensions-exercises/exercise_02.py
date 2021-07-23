# From the file nums.txt, sum all of the distinct numbers there.
filename = "../00-project-files/nums.txt"

sum_of_numbers = sum({int(one_line)
                      for one_line in open(filename)
                      if one_line.strip()})

print(sum_of_numbers)
