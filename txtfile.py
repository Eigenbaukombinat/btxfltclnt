import socket
import time
os = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ADDR =  ('195.201.94.166', 1234)

#reset
#os.sendto(b'\x1f\x2f\x42', ADDR)

#top left
#os.sendto(b'\x1fAA', ADDR)


import time


colors = {
    ' ':b'\x90 ',
    '0': b'\x90 ',
    '1': b'\x91 ',
    '2': b'\x92 ',
    '3': b'\x93 ',
    '4': b'\x94 ',
    '5': b'\x95 ',
    '6': b'\x96 ',
    '7': b'\x97 ',
}



res = b'\x1f\x2f\x42\x1fAA\x87\x90\x80'

with open('divoc.txt') as txtfile:
    lines = txtfile.readlines()


for line in lines:
    for z in line.strip("\n"):
        res += colors[z]
    res += b'\n\r'

os.sendto(res, ADDR)
