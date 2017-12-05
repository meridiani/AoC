#!/usr/bin/env python
###############################################################################
### Maria Duffy - December 2017
###
### Solution to Advent of Code day 3
###

from math import *
from numpy import *
import sys

### Read in number sequence from a file
f = open('input.txt')

### Convert the string to a float
x = float(f.read())
x = 30
### Close the input file
f.close()


### for count < x :
### work out each sum
### for each number wrk out the square it sits in
### corners are surrounded by 2 numbers 1 behind and 1 across
### sides are surrounded by 4 number 1 behind and 3 sitting in

myArray = [1,1,2,4,5,10,11,23,25] # 3 by 3 square to seed it
count = 9
cornerArray = []

while (count < x):
	memSum = 0

	### work out the square it is in and the squares corners
	### use this to work out the sum of surrounding
	### add the sum to an array
	i = count
	j = sqrt(i)
	
	if ((i%j) != 0):
		m = int((ceil(i/j)))
	else:
		m = int(j)

	### The square is always odd

	if ((m%2) == 0):
		m = int(m + 1)

	# work out the corners, they are always the sum of two
 
	l = m-1
	m2 = m**2

	n = m-2
	n2 = (m-2)**2
	p = n-1

	corners = [m2, m2-l, m2-2*l, m2-3*l]
	last_corners = [n2, n2-p, n2-2*p, n2-3*p]

	# find out what numbers we are dealing with

	### need to work out how to deal with the 3x3 side numbers
	
	cEl = 0
	for c in corners:
		if (count == c):
			elType = 'corner'
			break
		else:
			elType = 'side'
		cEl = cEl + 1

### now the hard part, the sum...
### for a corner the number is the one preceeding it and the one from the corner before
### x sum of x-1 and last value of tx

### let's get the sum working first

	### for side you want the last number plus three before it
	### work out the offset from centre
	### apply this to the row before
	### add/subtract 1 for correct 3 elements

	centre     = (m/2) + 1
	old_centre = centre - 1
	
	offset = i - (corners[cEl-1] - (centre - 1))

	print "centre is: ", centre, "aws: ", old_centre
	
	if (elType == 'corner'):
		memSum = myArray[count-1] + myArray[last_corners[cEl]]
	elif (elType == 'side'):
		memSum = myArray[count-1] + myArray[1] + myArray[1] + myArray[1]
	else:
		print "something has gone wrong"

	myArray.append(memSum)

   	count = count + 1

#print len(myArray),myArray
sys.exit()









### Take the square root of the file to find out the dimension of the grid

j = sqrt(i)

### We need to find the next highest square number

if ((i%j) != 0):
	m = int((ceil(i/j)))
else:
	m = int(j)

### The square is always odd

if ((m%2) == 0):
	m = m + 1

### So we have an m by m grid of numbers

print "grid is ", m, " by ", m

### Starting with top left corner as 1,1 where is number 1? i.e. centre element

centre = (m/2) + 1

### where is i in relation to the centre?


#it is a nesting set of squares
#my number is in the final square but where?
#how do you work out whether it is left right top or bottom???

#bottom has 5, left 4, top 4, right 4 so which bucket is it in?

### find corners of the square

l = m-1
m2 = m**2
### 25, 21, 17, 13 (m2, m2-l, m2-2l, m2-3l)
### square has 4 sides
### the number will always be in the outmost square
for k in arange(1,5):
	t1 = m2-((k-1)*l)
	t2 = m2-(k*l)
	
	if (t1 >= i > t2):
		if (k == 1):
			side = 'bottom'
			corner = t1
		elif (k == 2):
			side = 'left'
			corner = t1
		elif (k == 3):
			side = 'top'
			corner = t1
		elif (k == 4):
			side = 'right'
			corner = t1


offset = abs(i - (corner - (centre - 1)))

print "Answer is: ", (centre - 1) + offset

##############################################################################
print "OK to go!"
