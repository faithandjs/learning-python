import socket

host = '127.0.0.1'
port = 55556
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
msg = s.recv(1024)
s.close()

print(msg.decode())
