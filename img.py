import socket
import time
os = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ADDR =  ('195.201.94.166', 1234)

#reset
#os.sendto(b'\x1f\x2f\x42', ADDR)

#top left
#os.sendto(b'\x1fAA', ADDR)


from PIL import Image

import time

#img needs to be maximum 40x24px, edit colmap below
#according the colors used
img = Image.open('myfile.png')



maxx, maxy = img.size

print (img.size)

colors = {
    'black': b'\x90',
    'red': b'\x91',
    'green': b'\x92',
    'yellow': b'\x93',
    'blue': b'\x94',
    'magenta': b'\x95',
    'cyan': b'\x96',
    'white': b'\x97',
}

colmap = {
    2: 'white',
    1: 'red',
    0: 'black',
}
res = b'\x80'
for y in range(maxy):
    res += b'\x97    '
    for x in range(maxx):
        i = img.getpixel((x,y))
        st = colors[colmap[i]]
        res += bytes(st)+b' '
    res += b'\x97    \n\r'

os.sendto(res, ADDR)
