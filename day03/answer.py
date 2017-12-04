#!/usr/bin/env python
###############################################################################
### Maria Duffy - December 2017
###
### Solution to Advent of Code day 
###

from math import *
from numpy import *
import sys

### Read in number sequence from a file
f = open('input.txt')

### Convert the string to a float
i = float(f.read())
#i = 25
### Close the input file
f.close()

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
