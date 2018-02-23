import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 1111

s.bind(('',port))

s.listen(5)

while(True):
    c,addr = s.accept()
    print("Connection from", addr)
    message = raw_input(">>> ")
    
    c.send("Thank Mr.Client! Start chatting...\n")
    c.close()
