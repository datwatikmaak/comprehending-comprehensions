filename = "../00-project-files/mini-access-log.txt"

ip_addresses = [one_line.split()[0]
                for one_line in open(filename)]

# print(ip_addresses)

single_ip_addresses = {one_line.split()[0]
                       for one_line in open(filename)}

print(single_ip_addresses)
