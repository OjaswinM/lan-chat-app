import socket, threading

def acceptClient(server_socket):
    while True:
        socket, address = server_socket.accept()
        connected.append((address, socket))
        print("<" + str(address[0]) + ":" + str(address[1]) + ">", "is now connected.")
        serve = threading.Thread(target = serveClient, args = (address, socket))
        serve.start()

def serveClient(address, client):
    # print("started new thread for", client)
    while True:
        try:
            data = client.recv(4096).decode()
            print("<" + str(address[0]) + ":" + str(address[1]) + ">", data)
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

    # display = threading.Thread(target = printOnServer)
    # display.start()
