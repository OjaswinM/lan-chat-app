import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 1111

s.bind(('127.0.0.1',port))

s.listen(5)
conn, addr = s.accept()
print "Connected to", str(conn) + ": " + str(addr)

while(True):
    data = conn.recv(4096)
    print(data)
    message = raw_input('>')
    conn.send(message)
