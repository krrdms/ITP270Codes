"""
Based on Daniel Zappala's http://ilab.cs.byu.edu/python/code/echoserver-select.py
"""

import socket

host = 'localhost'
port = 12345
size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind process to socket and listen for traffic
sock.bind((host,port))
sock.listen(5)
print("Server starting: Listening on port %s" % port)
running = 1

#infinite loop - use select() to check for input
#select allows process to respond when input is available
#instead of "blocking" or waiting on input
while running:
    client, address = sock.accept()
    print('Client connected from', address)
    data = client.recv(size)
    print('%s: %s' % (client.getpeername(), data.decode().strip('\n')))

    if data:
        print ("data sent -->")
        client.send(data)

    else:
        client.close()

sock.close()