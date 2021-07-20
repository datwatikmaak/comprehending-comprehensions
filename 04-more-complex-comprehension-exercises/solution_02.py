filename = "../00-project-files/mini-access-log.txt"

print([one_line.split()[0]
       for one_line in open(filename)])
