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

		for x in line:
			m = [line/x for x in line]


f.close()

print "The sum is: ", sum
print "and the other one is: ", moduloSum

print "OK to go!" 
