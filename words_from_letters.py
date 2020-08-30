import json

def GenerateWordKey(word):
    key = "".join(sorted(set(word)))
    return key

with open("unique_letter_word_dictionary.json") as f:
    word_dictionary = json.load(f)

word = "word"
words = word_dictionary[GenerateWordKey(word)]
[print(word) for word in words]
print(len(words))
