import socket # Use the python socket library

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(('0.0.0.0', 9046))
s.listen()


s2, addr = s.accept()

# Print out the address of the client
print('Client Address is: ', addr)

# Receive the client's data from a socket
data = s2.recv(1024)

# Decode the received data
data = data.decode()

# Print the received data
print('Got this string: ' + data)

# Send back the encoded string to a socket
s2.sendall(data.encode())

# Close the socket's connection
s2.close()
