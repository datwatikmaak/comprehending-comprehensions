# TODO: From mini-access-log.txt, create a list of the IP addresses in that file.
file = [one_line.split(" - ")[0]
        for one_line in open("../00-project-files/mini-access-log.txt")]

print(file)
