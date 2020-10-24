import datetime
import socket
import subprocess
import time


def main():
    running = 1
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(10)
    while running:
        while True:
            results = None
            conn, address = server_socket.accept()  # accept new connection
            print("Connection from: " + str(address))
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            results = subprocess.Popen(data, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            conn.sendall(results)  # send data to the client
            time.sleep(2)
            conn.close()  # close the connection


if __name__ == '__main__':
    main()
