# Create a set comprehension from words (the Linux dictionary).
#
# Use that set comprehension to create a dict (using a dict comprehension). Ask the user to enter a sentence. The
# output dict will be the user's words, and the values will be True/False, indicating if the word is in the
# dictionary.

filename = "../00-project-files/words"

set_of_words = {one_word.strip()
                for one_word in open(filename)}

words = input("Enter a sentence: ")

word_in_sentence = {one_word: one_word in set_of_words
                    for one_word in words.lower().split()}

print(word_in_sentence)
