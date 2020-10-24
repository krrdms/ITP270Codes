import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending %s' % message)
    sock.sendall(message.encode())
    data = sock.recv(1024)
    print("received: %s" % data.decode())

finally:
    print('closing socket')
    sock.close()