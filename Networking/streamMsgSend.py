#!/usr/bin/python3
#send message to remote server via TCP, receive message back
import socket

s = socket.socket()

ipaddr = '172.16.1.15'
port = 5309

s.connect((ipaddr, port))

s.send(b'Jenny')

response, conn = s.recvfrom(1024)

print(response.decode())

s.close()
