from collections import Counter

filename = "../00-project-files/mini-access-log.txt"

ip_addresses = Counter([one_line.split()[0]
                        for one_line in open(filename)])

# nicely formatted table
for address, count in ip_addresses.items():
    print(f"{address:<20}{count}")
