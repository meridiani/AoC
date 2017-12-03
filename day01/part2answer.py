### Maria Duffy
### My solution to Day 1 - Advent of Code

from numpy import *
import sys

### First read in the numbers

myFile = open('myList.txt','r')

myString = myFile.read()

myFile.close()

stringLength = len(myString) - 1

### Fix the file so it has no extra character at some point

plusHalf = stringLength/2

sum = 0

for x in arange(0,(plusHalf)):

	if (myString[x]==myString[x+plusHalf]):
		
		sum = sum + int(myString[x])



### print to screen

print "The answer is: ", sum*2

print "OK to go!"
