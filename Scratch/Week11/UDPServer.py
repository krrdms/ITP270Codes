import socket


def makeBindUDPSocket(listenIP, listenPort):
    # Create a datagram socket
    _UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    _UDPServerSocket.bind((listenIP, listenPort))
    print("UDP server up and listening")
    return _UDPServerSocket


def main():
    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024

    UDPServerSocket = makeBindUDPSocket(localIP, localPort)

    # Listen for incoming datagrams
    while True:
        #recvfrom returns a tuple
        message, address = UDPServerSocket.recvfrom(bufferSize)
        print('client connected from', address)
        print('message from client:', message.decode())
        # Sending a reply to client
        bytesToSend = "Echo:".encode() + message
        address = address
        UDPServerSocket.sendto(bytesToSend, address)


if __name__ == '__main__':
    main()
