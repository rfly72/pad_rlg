add = lambda x, y: x+y
print add(5, 7)


subtract = lambda x, y: x-y
print subtract(3,1)

multiply = lambda x,y:x*y
print multiply(10,5) 


divide = lambda x,y:x/y
print divide(10,5)


exponent = lambda x,y:x**y
print exponent(2,3) 

square = lambda x:x**2
print square(5)

cube = lambda x:x**3
print cube(5)

squareroot = lambda x:x**0.5
print squareroot(81)

import math

sine = lambda x: math.sin(x*math.pi/180)
print sine(90)


cosine = lambda x: math.cos(x*math.pi/180)
print cosine(180)
    

def factorial (n):
    return reduce(lambda x,y:x*y,[1] +range(1,n+1))
print factorial(12)










