import socket

IPAddress = "127.0.0.1"
Port = 20003
bufferSize = 1024


def main():
    server_address = (IPAddress, Port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to %s port %s' %
          (server_address[0], server_address[1]))
    sock.connect(server_address)

    try:
        userInput = input("Enter Text to Send:")
        sock.sendall(userInput.encode())
        data = sock.recv(bufferSize)
        print("received: %s" % data.decode())
    finally:
        sock.close()


if __name__ == '__main__':
    main()
