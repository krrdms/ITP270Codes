import datetime
import socket


def main():
    running = 1
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(5)
    while running:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            data = str(datetime.datetime.utcnow())
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    main()
