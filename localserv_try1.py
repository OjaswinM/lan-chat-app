import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 11113

s.bind(('',port))

s.listen(5)
c,addr = s.accept()
c.send("Thank Mr.Client! It is I who talks\n")
while(True):

    print("Connection from", addr)
    message = raw_input(">>> ")
    if message == 'exit':
        c.close()
    else:
        c.send(message)
