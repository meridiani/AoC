#!/usr/bin/env python
###############################################################################
### Maria Duffy - December 2017
###
### Solution to Advent of Code day 4
###

import sys

### Open file, make each line a list
### Iterate over the list and see if there are any matches
### Is there a function that does this?

### Invalid if same

f = open('input.txt','r')

isValid = 0

myList = []

with open('input.txt') as f:
    for line in f:
        line = line.split() # to deal with blank 
	alphaLine = sorted(line)
	sortedLine = []
	for word in alphaLine:
		b = sorted(word)
		newWord = ''.join(b)
		sortedLine.append(newWord)

	newList = set(sortedLine)
	#newList = set(line)
	if len(newList) == len(line):
		isValid = isValid + 1

f.close()

print "This many are valid passphrases: ", isValid
###############################################################################
print "OK to go!"
