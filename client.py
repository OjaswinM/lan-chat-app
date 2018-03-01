import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 1111

c.connect(('127.0.0.1',port))

while(True):
    message = raw_input('>')
    c.send(message)
    data = c.recv(4096)
    print "Message from server: ", data
