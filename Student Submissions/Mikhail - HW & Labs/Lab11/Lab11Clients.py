import socket
# -----TCP Client-----
localIP = "127.0.0.1"
localPort = 20003
buffersize = 1024

def tcpClient():
    address = (localIP, localPort)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    print('Connecting to ', address[0], address[1])
    try:
        userInput = input("Type something: ")
        sock.sendall(userInput.encode())
        data = sock.recv(buffersize)
        print('Received: %s' % data.decode())
    finally:
        sock.close()


# -----UDP Client-----
def udpClient():
    localPort = 20001
    localIP = "127.0.0.1"
    bufferSize = 1024

    address = (localIP, localPort)
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        userInput = input('Type something: ')
        sock.sendto(userInput.encode(), address)
        data = sock.recvfrom(bufferSize)
        print('Received  %s' % data[0].decode())
        userInput = input('Type something else: ')
    finally:
        sock.close()

def main():
    print('1 -> Start TCP Client\n2 -> Start UDP Client')
    while True:
        x = int(input('\nEnter which client you want to run: '))
        if x == 1:
            tcpClient()
            break
        if x == 2:
            udpClient()
            break
        else:
            break
main()
