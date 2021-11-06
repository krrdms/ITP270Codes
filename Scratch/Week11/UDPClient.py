import socket

IPAddress = "127.0.0.1"
Port = 20001
bufferSize = 1024


def main():
    serverAddressPort = IPAddress, int(Port)
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    userInput = input("Enter Text to Send:")
    while userInput:
        sock.sendto(userInput.encode(), serverAddressPort)
        data = sock.recvfrom(bufferSize)
        print("received: %s" % data[0].decode())
        userInput = input("Enter Text to Send:")


if __name__ == '__main__':
    main()
