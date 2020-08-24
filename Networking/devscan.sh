#!/bin/bash

echo "Enter IP to scan 1-65535 ports on."
read address

for i in {1..65535};

do
    echo >/dev/tcp/$address/$i &&
    echo "port $i is open on $address" >> $address\_openports.txt ||
    &>/dev/null

done
