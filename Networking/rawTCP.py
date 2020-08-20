#!/usr/bin/python3

import socket
import sys
import binascii
import array

from struct import *

def chksum(data):
    if len(data) % 2 != 0:
        data += b'\0'
    res = sum(array.array("H", data))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16
    return (~res) & 0xffff

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

packet = ''

src_ip = "66.66.66.66"
dst_ip = "172.16.40.10"

ip_ver_ihl = 69     #0x45
ip_tos = 0
ip_len = 0
ip_id = 2020
ip_frag = 0
ip_ttl = 64
ip_proto = 6       #tcp
ip_check = 0
ip_srcadd = socket.inet_aton(src_ip)
ip_dstadd = socket.inet_aton(dst_ip)

ip_header = pack('!BBHHHBBH4s4s', ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd) 


#TCP HEADER
src_port = 54321
dst_port = 1234
seq_number = 90210
ack_number = 30905
off_res = 80 #size of tcp header
flags = 2
window = socket.htons(5840)
checksum = 0
urg_ptr = 0
#options = 0

tcp_header = pack('!HHLLBBHHH', src_port, dst_port, seq_number, ack_number, off_res, flags, window, checksum, urg_ptr)


message = b'damessage'

#pseudo header fields

placeholder = 0
protocol = socket.IPPROTO_TCP
tcp_length = len(tcp_header) + len(message)

psh = pack('!4s4sBBH', ip_srcadd, ip_dstadd, placeholder, protocol, tcp_length) 
psh = psh + tcp_header + message

print(psh)
tcp_check = chksum(psh)

#create tcp header again w/ checksum

tcp_header = pack('!HHLLBBH', src_port, dst_port, seq_number, ack_number, off_res, flags, window) + pack('H',tcp_check) + pack('!H', urg_ptr)

packet = ip_header + tcp_header + message

s.sendto(packet, (dst_ip, 0))
