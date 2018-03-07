import socket, threading

def reciveFromServer(client_socket):
    while True:
        try:
            serverMessage = client_socket.recv(4096).decode()
            print(serverMessage)
        except:
            pass

if __name__ == '__main__':
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = 'localhost'
    port = 12349

    c.connect((host, port))

    fromServer = threading.Thread(target = reciveFromServer, args = (c, ))
    fromServer.start()

    while(True):
        message = input('>')
        c.send(message.encode())
        if message == 'quit':
            c.close()
            break
