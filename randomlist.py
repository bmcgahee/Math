import math

squareRootList = dir(math.sqrt) #gets the list of built-in functions for the math.sqrt() function
size = len(squareRootList)

print "Function ", "Type"
for i in range(0, size):
    print squareRootList[i], type(squareRootList[i]) #displays each built-in function and its type

print "There are " + str(size) + " built-in functions."

