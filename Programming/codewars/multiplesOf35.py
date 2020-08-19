#!/usr/bin/python3

thesum = 0

for i in range(10):
    if (i % 3 == 0) or (i % 5 == 0):
        thesum += i

print(thesum)
