# TODO: Create a dictionary (or a variant thereof -- such as Counter) in which the keys are the IP addresses and the
#  values are the number of times that each IP address appeared in the file.  Use the resulting dict/Counter to print
#  each IP address and its times
import collections


file = [one_line.split(" - ")[0]
        for one_line in open("../00-project-files/mini-access-log.txt")]

print(collections.Counter(file))
