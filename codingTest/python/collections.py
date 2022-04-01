from collections import Counter

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

word = "hello world"
print(Counter(word) == countLetters(word)) # True
print(Counter(word).most_common()[0]) # ('l', 3)