def f(x):
    y = x*x + 5
    return y

def g(x):
    y = x - 2
    return y

def fog(x):
    t = g(x)
    y = f(t)
    return y

def gof(x):
    t = f(x)
    y = g(t)
    return y

#Test 1
fy = f(3) #f(3) = 3^2 + 5 = 14
gy = g(3) #g(3) = 3 - 2 = 1

print "f(3) = " + str(fy)
print "g(3) = " + str(gy)

#Test 2
fog = fog(-2) #f(g(-2)) = f(-4) = (-4)^2 + 5 = 21
gof = gof(-2) #g(f(-2)) = g(9) = 9 - 2 = 7

print "f(g(-2)) = " + str(fog)
print "g(f(-2)) = " + str(gof)

    
