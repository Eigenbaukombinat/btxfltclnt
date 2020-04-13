import socket

os = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nick = input('What is your nickname? > ')

while True:
    got = input('<{}> '.format(nick.strip()))
    if got == 'exit':
        break
    if got == 'clear':
        os.sendto(b'\x1f\x2f\x42\x1fAA\x87\x90', ('195.201.94.166', 1234))
    else:
        os.sendto(bytes('<{}> {}\r\n'.format(nick, got), 'ascii'), ('195.201.94.166', 1234))
