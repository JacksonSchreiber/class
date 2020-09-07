#!/usr/bin/python3


def rgb(r, g, b):
    l = [r, g, b]
    newHex = ""
    for i in range(len(l)):
        if l[i] > 255: #round
            l[i] = 255
        elif l[i] < 0:
            l[i] = 0
        byte = (hex(l[i]).lstrip("0x")).upper() #int to hex
        byte = "0"*(2-len(byte)) + byte #add "0" buffer
        newHex += byte

    return newHex 


print(rgb(1, 1, 255))
