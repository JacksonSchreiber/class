#!/usr/bin/python3
def move_zeros(array):
    x = 0
    for i in range(len(array) - 1, -1, -1): #iterate backwards
        if isinstance(array[i], (int, float)) and not isinstance(array[i], bool): #check if int or float and not bool
            if  array[i] == 0:
                array.pop(i)
                array.append(0)
    return array
print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
