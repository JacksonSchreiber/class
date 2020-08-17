#!/usr/bin/python3


def digital_root(n):
    
    nsum = 0

    for x in str(n):
        nsum += int(x)
    if len(str(nsum)) == 1:
        return nsum

    return digital_root(nsum)


print(digital_root(493193))
