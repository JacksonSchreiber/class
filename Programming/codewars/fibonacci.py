#!/usr/bin/python3

#STANDARD RECURSIVE FIBONACCI SEQUENCE
#def fibonacci(n, *args):
#    if n in [0, 1]:
#        return n
#    return fibonacci(n - 1) + fibonacci(n - 2)

#print(fibonacci(20)


#CACHED RECURSIVE FIBONACCI SEQUENCE
aa = {0:0, 1:1} #define first two
def fibonacci(n):
    if n in aa:
        return aa[n]
    else:
        aa[n] = fibonacci(n-1) + fibonacci(n-2) 
        return aa[n]

print(fibonacci(500))
