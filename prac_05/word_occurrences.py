"""
Word Occurrences
Estimate: 40 minutes
Actual:    minutes
"""
word_to_occurrences = {}
sentence = input("Give us a string: ")
words = sentence.split()
print(words)
for word in words:
    if word in word_to_occur