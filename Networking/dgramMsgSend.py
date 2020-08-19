#!/usr/bin/python3
#Send message  to localhost server via UDP, receive message back
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ipaddr = '127.0.0.1'
port = 10000


s.connect((ipaddr, port))

s.send(b'Disturbed')

response, conn = s.recvfrom(1024)

print(response.decode())
