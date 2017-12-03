### Day 2

### First lead in each line as a list
### Find min and max for each
### Do difference
### Sum the differences

sum = 0
moduloSum = 0

with open('input.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            	line = [int(i) for i in line]
            	polyShape.append(line)
		sum = sum + (max(line) - min(line))

# so how do I go through each number and work out the division?

		for x in line:
			for d in line:
				if x%d == 0:
					i = float(x)/float(d)
					if (i != 1.0):
						moduloSum = moduloSum + i

f.close()

print "The sum is: ", sum
print "and the other one is: ", moduloSum

print "OK to go!" 
