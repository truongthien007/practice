"""
Word Occurrences
Estimate: 40 minutes
Actual:  55 minutes
"""
word_to_occurrence = {}
sentence = input("Give us a string: ")
words = sentence.split()
words.sort()
for i in range(0, len(words)):
    if words[i] not in word_to_occurrence:
        # word_to_occurrence[words[i]] is value
        word_to_occurrence[words[i]] = 1
    else:
        word_to_occurrence[words[i]] += 1

print(word_to_occurrence)
for k, v in word_to_occurrence.items():
    print(f'{k: <13}: {v}')
