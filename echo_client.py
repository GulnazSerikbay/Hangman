
import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9056))


s.sendall(input("enter your word... ").encode())

data = s.recv(1024)

print('Your word is: ' + data.decode() + "\nWait until your counterpart ends the game...")


s.close()
