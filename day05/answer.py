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

myList = [0,3,0,1,-3]

steps = 0

### We have the list of ints so now we need to move around

listLen = len(myList)

x = 0

inside = True

while (inside):
	n = myList[x]
	print (x-n), x, n

	if (abs(n)>=3):
		myList[x] = n - 1
	else:
		myList[x] = n + 1

	x = x + n

	steps = steps + 1	
	
	print "hello", myList

	if (listLen > x):
	
		continue

	else:
		inside = False

#print "Final list is: ", myList	
print "Steps taken to exit: ", steps

###############################################################################
print "OK to go!"
