# Wordle Solver 
Little python script + dictionary to help solve Wordle puzzles

## Usage
Usage: ./wordlesolve.py <letters in word> <placement>

- <letters in word> is just any letters that you know are in the word, without spaces, for example: vr
- <placement> should have the actual placement for any letters that went green, with any unknowns marked as an underscore, for example __v_r

## Demo

```
wordlesolver$ python3 ./wordlesolver.py f __v_r
Loaded 15918 words from dictionary.
favor
fever
fiver
```

## Protip

Try to use as many vowels as possible on the first guess, my first guess is always adieu.
