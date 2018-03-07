import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 1111

c.connect(('localhost', port))

while(True):
    message = input('>')
    c.send(message.encode())
