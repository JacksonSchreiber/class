#!/bin/bash

echo "Enter NTW address (ex 192.168.1):"
read net
echo "Enter starting host range (ex 1):"
read start
echo "Enter ending host range (ex 254):"
read end
echo "Enter ports space-delimited (ex 20 21 22 23 80):"
read ports

for ((i=$start; $i<=$end; i++))
do
        nc -n -v -z -w1 $net.$i $ports 2>&1 | grep open
done
