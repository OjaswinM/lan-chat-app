import socket, threading

def acceptClient(server_socket):
    while True:
        socket, address = server_socket.accept()
        # connected.append((address, socket))
        # print("<" + str(address[0]) + ":" + str(address[1]) + ">", "is now connected.")
        socket.send("Welcome to the server! Please enter your name:- ".encode())
        name = socket.recv(4096).decode()
        connected.append((address, socket, name))
        print( name + " is now connected.")
        serve = threading.Thread(target = serveClient, args = (address, socket, name))
        serve.start()

def serveClient(address, client, name):
    # print("started new thread for", client)
    while True:
        try:
            data = client.recv(4096).decode()
            if data == 'quit':
                # data = "is disconnecting.."
                # print("<" + str(address[0]) + ":" + str(address[1]) + ">", data)
                message =  name + " is disconnecting..."
                print(message)
                break
            elif data == '':
                break
            else:
                message = "<" + name + "> " + data
                print(message)
            broadcast(client, name, message)
        except:
            pass

def broadcast(currentClient, name, message):
    for client in connected:
        if currentClient not in client:
            client[1].send(message.encode())


if __name__ == '__main__':
    connected = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '192.168.0.4'
    port = 12352

    s.bind((host, port))

    s.listen(5)

    print("Server hosted.")

    accept = threading.Thread(target = acceptClient, args = (s, ))
    accept.start()
