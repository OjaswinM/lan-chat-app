import socket, threading

def reciveFromServer(client_socket):
    while True:
        try:
            serverMessage = client_socket.recv(4096).decode()
            print("\r" + serverMessage)
        except:
            pass

def sendToServer(client_socket):
    while(True):
        message = input('>')
        client_socket.send(message.encode())
        if message == 'quit':
            c.close()
            break

if __name__ == '__main__':
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = '192.168.0.4'
    port = 12355

    c.connect((host, port))

    fromServer = threading.Thread(target = reciveFromServer, args = (c, ))
    fromServer.start()

    toServer = threading.Thread(target = sendToServer, args = (c, ))
    toServer.start()
