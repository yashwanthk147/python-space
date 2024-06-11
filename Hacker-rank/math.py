

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def multiplication():
    mul = a * b
    return mul

def substarction():
    sub = a - b
    return sub

def addition():
    add = a + b
    return add

result = multiplication()
result1 = addition()
result2 = substarction()
print(result)
print(result1)
print(result2)