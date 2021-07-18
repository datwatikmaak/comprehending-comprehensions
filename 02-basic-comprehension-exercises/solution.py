mylist = [10, 20, 30]
joined = "*".join([str(x) for x in mylist])
print(joined)


hexnums = input("Enter some hex numbers: ").split()    # 1234 5678 90ab cdef
total = sum([int(x, 16) for x in hexnums])
print(total)


words = input("Enter some words: ")    # This is a bunch of words
char_count = sum([len(one_word) for one_word in words.split()])
print(char_count)
