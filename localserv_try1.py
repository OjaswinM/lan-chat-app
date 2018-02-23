import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 11133

s.bind(('',port))

s.listen(5)
c1,addr = s.accept()
print("Connection from", addr)
while(True):
    message = raw_input("> ")
    c1.send(message)
    recv = c1.recv(2048)
    print "Client: ", recv
