#Author: Ben McGahee
#Title: Complex Numbers
#Date: 5/4/2016 (May the 4th be with you! :))
#Purpose: This program uses the cmath module to perform various operations on complex numbers in the form a + bj, where j = sqrt(-1)

import cmath #math module for complex numbers

z1 = 2 - 3j
z2 = 1 + 4j

realZ1 = z1.real #these are the real and imaginary parts of z1 and z2
imagZ1 = z1.imag
realZ2 = z2.real
imagZ2 = z2.imag

z1Conj = 2 + 3j #conjugate of z1
z2Conj = 1 - 4j #conjugate of z2

zAdd = z1 + z2
zSubtract = z1 - z2
zMultiply = z1 * z2
zDivide = z1 / z2

z1ConjProd = z1 * z1Conj
z2ConjProd = z2 * z2Conj

print "The real parts of z1 and z2 respectively are: " + str(realZ1) + " and " + str(realZ2)
print "The imaginary parts of z1 and z2 respectively are: " + str(imagZ1) + " and " + str(imagZ2)
print "The sum of z1 and z2 is: " + str(zAdd)
print "The difference of z1 and z2 is: " + str(zSubtract)
print "The product of z1 and z2 is: " + str(zMultiply)
print "The quotient of z1 and z2 is: " + str(zDivide)
print "The product of z1 and its conjugate is: " + str(z1ConjProd)
print "The product of z2 and its conjugate is: " + str(z2ConjProd) #the last two products should be real numbers




