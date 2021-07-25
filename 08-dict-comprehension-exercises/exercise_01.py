# Ask the user for a sentence, and then create a dict based on that sentence, in which the keys are the words and the
# values are the "scores" for the words.

def word_score(word):
    return sum([ord(letter) - 96
                for letter in word.lower()])


words = input("Please enter some words: ")

score_dict = {one_word: word_score(one_word)
              for one_word in words.split()}

print(score_dict)
