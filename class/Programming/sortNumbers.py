#!/usr/bin/env python3
#Recursive sorting algorithm


l = [5, 4, 10, 2, 1, 20, 12, 1, 1, 500, 20]

def sorting(y, l): #y is current index
    swapped = False #if any change to list, set True
    for x in range(y, -2, -1):
        print(x, l)
        if l[x] > l[x+1] and x != -1: #if x > x+1, swap them
            swapped = True
            temp = l[x]
            l[x] = l[x+1]
            l[x+1] = temp
            print(x, l)
    if swapped == True: #if any change in list, call sorting
        sorting(y, l)
    pass


print(l)
for i in range(len(l)):
        if i != len(l) - 1:
            if l[i] > l[i+1]: # if i > i+1, swap spots
                sorting(i, l) #send current index to sorting

print(l)




