import socket

localIP = '127.0.0.1'
localPort = 20003
bufferSize = 1024


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((localIP, localPort))
    sock.listen(5)
    print("Server starting: Listening on port %d" % localPort)

    while True:
        conn, address = sock.accept()
        try:
            print('client connected from', address)
            data = conn.recv(bufferSize)
            print(conn.getpeername(), 'data received', data.decode())
            if data:
                bytesToSend = "Echo:".encode() + data
                conn.sendall(bytesToSend)
                print("data sent -->", bytesToSend.decode())
            else:
                print("no data")
        finally:
            conn.close()


if __name__ == '__main__':
    main()
