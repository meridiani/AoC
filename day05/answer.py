#!/usr/bin/env python
###############################################################################
### Maria Duffy - December 2017
###
### Solution to Advent of Code day 
###

import sys

f = open('input.txt','r')

myList = []
for line in f:
	myList.append(int(line))
f.close() 

steps = 0

### We have the list of ints so now we need to move around

listLen = len(myList)

x = 0

while x < listLen:

	x = myList[x]


	print x

	sys.exit()

#x = myList[startHere]
#change myList[startHere+1]
#goto myList[x]

#rinse and repeat

###start at first elements, increment that by one and move to the next one

print "Steps taken to exit: ", steps

###############################################################################
print "OK to go!"
