
import socket
import time


def main():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    message = input("enter command:")
    data = None
    while message.lower().strip() != 'bye':
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        client_socket.send(message.encode())  # send message
        while not data:
            data = client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
        message = input("enter command:")
        client_socket.close()  # close the connection
        client_socket = None
        data = None

if __name__ == '__main__':
    main()
