import socket, threading, pickle

def reciveFromServer(client_socket):
    while True:
        try:
            serverMessage = client_socket.recv(4096).decode()
            if serverMessage == "/printusers":
                print("i am pringint list of users hehexd")
                dataStream = client_socket.recv(4096).decode()
                connected = pickle.loads(dataStream)
                print(connected)
            else:
                print("\r" + serverMessage)
        except:
            pass

def sendToServer(client_socket):
    while(True):
        message = input()
        client_socket.send(message.encode())
        if message == 'quit':
            break

if __name__ == '__main__':
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = 'localhost'
    port = 12352

    c.connect((host, port))

    fromServer = threading.Thread(target = reciveFromServer, args = (c, ))
    fromServer.start()

    toServer = threading.Thread(target = sendToServer, args = (c, ))
    toServer.start()
