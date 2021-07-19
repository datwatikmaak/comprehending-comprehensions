# file = [one_line
#         for one_line in open("../sample.txt")]
#
# print(file)


file = [one_line.split(":")[0]
        for one_line in open("../password-file.txt")
        if not one_line.startswith("g")]

print(file)
