filename = "../00-project-files/linux-etc-passwd.txt"

print([tuple(one_line.split(":")[:3:2])    # expression
      for one_line in open(filename)    # source
      if one_line.strip() and not one_line.startswith("#")])    # filtering
