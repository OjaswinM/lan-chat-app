import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 11111

c.connect(('127.0.0.1',port))

while(True):
    print c.recv(1024)
