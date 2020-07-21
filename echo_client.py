
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('unix-02.qatar.cmu.edu', 9046))

s.sendall('Gulnaz Serikbay'.encode())

data = s.recv(1024)

print('You have this: ' + data.decode())
