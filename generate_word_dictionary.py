import json

def GenerateWordKey(word):
    key = "".join(sorted(set(word)))
    return key

with open('words_alpha.txt') as f:
    lines = [line.rstrip() for line in f]

wordkeys = [GenerateWordKey(item.replace("\n", "")) for item in lines]

initial = []
letterDictionary = dict.fromkeys(wordkeys, initial)

for word in lines:
    wordkey = GenerateWordKey(word)
    current_list = letterDictionary[wordkey].copy()
    current_list.append(word)
    letterDictionary.update({wordkey:current_list})

filename = "unique_letter_word_dictionary.json"
with open(filename, 'w') as outfile:
    json.dump(letterDictionary, outfile)


