words = "This is a bunch of words and a bunch of words this is"

single_words = {word
                for word in words.split()}

print(single_words)

len_single_words = {len(word)
                    for word in words.split()}

print(len_single_words)

sum_single_words = sum({len(word)
                        for word in words.split()})

print(sum_single_words)
