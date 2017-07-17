a = [10, 11, 12]
b = [4, 5, 6]
add = map(lambda x,y:x+y, a,b)
print add

subtraction = map(lambda x,y:x-y, a,b)
print subtraction

multiply = map(lambda x,y:x*y, a,b)
print multiply

divide = map(lambda x, y: x/y, a,b)
print divide

square = map(lambda x:x**2,a)
print square

squareroot = map(lambda x:x**0.5, b)
print squareroot

cube = map(lambda x: x**3, b)
print cube

import math 


factorial=map(lambda x : math.factorial(x), b )
print factorial

list = [0, 90, 45]
sine = map(lambda x: math.sin(x*math.pi/180), list )
print sine

cosine = map(lambda x: math.cos(x*math.pi/180), list)
print cosine