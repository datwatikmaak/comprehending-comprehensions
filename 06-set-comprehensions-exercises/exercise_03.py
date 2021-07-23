# From linux-etc-passwd.txt, show all of the different shells.
filename = "../00-project-files/linux-etc-passwd.txt"

shells = {line.rstrip().split(":")[-1]
          for line in open(filename)
          if not line.startswith("#") and line.strip()}

print(shells)
