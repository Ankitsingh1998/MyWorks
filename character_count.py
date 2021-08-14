#Character count in a sentence/word and saving to dictionary
text = input('Enter a word/sentence: ')
dictionary = {}
for letter in text:
    if letter in dictionary:
        dictionary[letter] = dictionary[letter] + 1
    else:
        dictionary[letter] = 1
        
print(dictionary)
print(dictionary[input('Enter a letter or special character: ')])

#collections library to count letters in a word/sentence
from collections import Counter
text = input('Enter a word/sentence: ')

def letter_count(text):
    return dict(Counter(text))

print(letter_count(text))

#Character count using for loop
myStr = input('Enter a word/sentence: ')

counter = {}
for char in myStr:
    if char in counter:
        counter[char] = counter[char] + 1
    else:
        counter[char] = 1
print(counter)
