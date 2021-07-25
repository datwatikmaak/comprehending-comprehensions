# Repeat Exercise 1, but ignore in the dict output any word that has < 3 letters or > 7 letters.
def word_score(word):
    return sum([ord(letter) - 96
                for letter in word.lower()])


words = input("Please enter some words: ")

score_dict = {one_word: word_score(one_word)
              for one_word in words.split()
              if len(one_word) >= 3 and len(one_word) <= 7}

print(score_dict)
