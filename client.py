import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 1111

c.connect(('127.0.0.1',port))

while(True):
    message = raw_input('>')
    if message == 'quit':
        c.send("Disconnecting")
        c.close()
        break
    c.send(message)
