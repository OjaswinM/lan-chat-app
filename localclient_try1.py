import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 11133

c.connect(('127.0.0.1',port))

while(True):
    serv = c.recv(2048)
    print "Server: ", serv
    message = raw_input(">")
    c.send(message)
