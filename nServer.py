import socket, threading

def acceptClient(server_socket):
    while True:
        socket, address = server_socket.accept()
        name = socket.recv(1024)
        connected.append((name, socket))
        print(name, "is now connected.")

def printOnServer():
    while True:
        for users in connected:
            try:
                data = users[1].recv(4096).decode()
                print(data)
                if not data:
                    pass
            except:
                pass


if __name__ == '__main__':
    connected = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 1111

    s.bind((host, port))

    s.listen(5)

    print("Server hosted.")

    accept = threading.Thread(target = acceptClient, args = (s, ))
    accept.start()

    display = threading.Thread(target = printOnServer)
    display.start()
