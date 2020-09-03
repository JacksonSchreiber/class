#!/usr/bin/python3.8

def dirReduc(arr):

    d = { 'NORTH':-1, 'WEST':-2, 'SOUTH':1, 'EAST':2 } #define opposite directions. when added, they equal 0
    
    i = len(arr) - 1 #iterate through list backwards
    while i > 0:
        if d[arr[i]] + d[arr[i-1]] == 0: #if arr[i] and arr[i-1] are opposite, remove both
            arr.pop(i)
            arr.pop(i-1)
            i = len(arr) - 1 #reset iteration
            continue
        i -= 1
    return arr 
       




arr = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
print(dirReduc(arr))
