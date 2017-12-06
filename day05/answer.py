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

inside = True

while (inside):
	n = myList[x]
	
	myList[x] = n + 1

	x = x + n

	steps = steps + 1	

	if (listLen > x):
	
		continue

	else:
		inside = False
	
print "Steps taken to exit: ", steps

###############################################################################
print "OK to go!"
