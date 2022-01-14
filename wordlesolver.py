#!/usr/bin/python3

import sys, string, re

# split a word into an array of characters
def split(word):
    return [char for char in word]

# validate args
if len(sys.argv) != 3:
    print("Usage: ./wordlesolve.py <letters in word> <placement>")
    print("<letters in word> is just any letters that you know are in the word, without spaces, for example: vr")
    print("<placement> should have the actual placement for any letters that went green, with any unknowns marked as an underscore, for example __v_r")
    exit()

dictionary = open("words.txt", "r")
words = dictionary.readlines()
print("Loaded " + str(len(words)) + " words from dictionary.")
dictionary.close()

# this will be the array with the possible answers
solutions = []

# remove new lines from words in array, put them into solutions array
for word in words:
   solutions.append(word.strip())

# remove words without the necessary chars
solutions = [x for x in solutions if all(y in x for y in sys.argv[1])]

# do some checks to the user regex
def errorout():
    print("Second argument should be exactly 5 characters long, consisting of letters and un      derscores only")
    exit()

regex = sys.argv[2]
allowed = set(string.ascii_lowercase + '_')
if not set(regex) <= allowed:
    errorout()
if len(regex) != 5:
    errorout()
    
regex = regex.replace("_", ".")

# match based on regex
regex_pattern = "^" + regex + "$"
pattern = re.compile(regex_pattern)

for word in solutions:
    if pattern.match(word):
        print(word)
