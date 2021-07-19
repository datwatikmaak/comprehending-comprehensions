def reverse_word(word):
    return word[::-1]


# met split() maak je een list van de woorden die de gebruiker invoert.
words = input("Enter some words: ").split()

reverse = [reverse_word(one_word)
           for one_word in words]

print(reverse)
