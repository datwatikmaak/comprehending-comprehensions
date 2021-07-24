filename = "../00-project-files/linux-etc-passwd.txt"

result = {line.split(":")[0]: line.split(":")[2]
          for line in open(filename)
          if line.strip() and not line.startswith("#")}

# print(result)

# dict comprehension with a sentense
words = "This is a bunch of words"

my_word_dict = {one_word: len(one_word)
                for one_word in words.split()
                if not one_word.startswith(("a", "e", "i", "o", "u"))}

print(my_word_dict)
