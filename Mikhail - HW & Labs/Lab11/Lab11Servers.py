import socket


# -----TCP Server-----
def tcpServer():
    localIP = "127.0.0.1"
    localPort = 20003
    bufferSize = 1024

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (localIP, localPort)
    sock.bind(address)
    sock.listen(1)
    print('Server listening...')

    while True:
        conn, address = sock.accept()
        try:
            print('Connection from: ', address)
            data = conn.recv(bufferSize)
            print('Received data: ', data.decode())
            if data:
                bytesToSend = "Echo: ".encode() + data
                conn.sendall(bytesToSend)
                print('[+] Data was sent!')
            else:
                print('[!] No data')
        finally:
            conn.close()


# -----UDP Server-----
def udpServer():
    localPort = 20001
    localIP = "127.0.0.1"
    bufferSize = 1024

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    address = (localIP, localPort)
    sock.bind(address)
    print('Socket created and bound to %s %d' % (localIP, localPort))
    while True:
        message, address = sock.recvfrom(bufferSize)
        print('Connection from:', address)
        print('Message:', message.decode())
        bytesToSend = "Echo: ".encode() + message
        sock.sendto(bytesToSend, address)


def main():
    print('1 -> Start TCP Server\n2 -> Start UDP Server')
    x = int(input('\nEnter which server you want to run: '))
    while True:
        if x == 1:
            tcpServer()
            break
        if x == 2:
            udpServer()
            break
        else:
            break


main()
