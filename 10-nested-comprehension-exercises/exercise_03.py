# Produce a list of the unique octets (from the IP addresses) in mini-access-log.

unique_octets = list({one_octect
                      for one_line in open("../00-project-files/mini-access-log.txt")
                      for one_octect in one_line.split()[0].split(".")})

print(unique_octets)
