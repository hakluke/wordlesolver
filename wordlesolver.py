#!/usr/bin/python3

import sys, string, re

# split a word into an array of characters
def split(word):
    return [char for char in word]

# validate args
if len(sys.argv) != 4:
    print("Usage: ./wordlesolver.py <letters in word> <letters not in word> <placement>")
    print("<letters in word> is just any letters that you know are in the word, without spaces, e.g. vr")
    print("<letters not in word> is any letters that you know are NOT in the word, without spaces, e.g. qxu")
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

# check sys.argv[1] and sys.argv[2]
allowed = set(string.ascii_lowercase + '?')
if not set(sys.argv[1] + sys.argv[2]) <= allowed:
   print("The first and second arguments should either be lowercase letters, or a single question mark (?) as a placeholder") 

# remove words without the necessary chars
if sys.argv[1] != '?':
    solutions = [x for x in solutions if all(y in x for y in sys.argv[1])]

# remove words with characters that we know aren't in the solution
if sys.argv[2] != '?':
    solutions = [x for x in solutions if all(y not in x for y in sys.argv[2])]

# do some checks to the user regex
def errorout():
    print("Second argument should be exactly 5 characters long, consisting of letters and underscores only")
    exit()

regex = sys.argv[3]
if regex == '?':
    regex = "_____"
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
