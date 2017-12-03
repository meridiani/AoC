### Maria Duffy
### My solution to Day 1 - Advent of Code

from numpy import *

### First read in the numbers

myFile = open('myList.txt','r')

myString = myFile.read()

myFile.close()

stringLength = len(myString)

### Fix the file so it has no extra character at some point
if (myString[0]==myString[-2]):
	print "Oh no first and last match!"

	sum = 0

	for x in arange(1,stringLength):
		if (myString[x-1]==myString[x]):
			sum = sum + int(myString[x])
	sum = sum + int(myString[0]) 

else:
	print "No circles here thank goodness!"
	print "First is: ", myString[0], "Last is: ", myString[-1]
### How to make it a circular list?

### maybe break into two strings at a point where they aren't the same then
### rejoin at so first and last def not the same

### loop through list and find repeats

### and these to a list

### sum the numbers

### print to screen

print "The answer is: ", sum

print "OK to go!"
