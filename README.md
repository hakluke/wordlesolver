# Wordle Solver 
Little python script + dictionary to help solve Wordle puzzles

## Usage
Usage: ./wordlesolver.py [letters in word] [letters not in word] [placemen]t

- [letters in word] is just any letters that you know are in the word, without spaces, for example: fa
- [letters not in word] is just any letters that you know are not in the word, without space, for example: bqwetl
- [placement] should have the actual placement for any letters that went green, with any unknowns marked as an underscore, for example f___r

 ### Important
 If you can't fill out one of these fields because you don't yet have enough information, just replace it with a single question mark "?".=

## Demo

```
wordlesolver$ python3 wordlesolver.py fa bqwetl f___r
Loaded 15918 words from dictionary.
fakir
favor
fchar
friar
```

## Protip

- Try to use as many vowels as possible on the first guess, my first guess is always adieu.
- Actually, according to [this](https://www.reddit.com/r/wordle/comments/s3fjmw/all_the_best_starting_words_ranked_mathematically/) you might be better to use `roate` as your first guess!
