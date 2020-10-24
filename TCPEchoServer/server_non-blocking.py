"""
Based on Daniel Zappala's http://ilab.cs.byu.edu/python/code/echoserver-select.py
"""

import select
import socket
import datetime

host = 'localhost'
port = 12345
backlog = 5
size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Release listener socket immediately when program exits,
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind process to socket and listen for traffic
sock.bind((host,port))
sock.listen(5)
print("Server starting: Listening on port %s" % port)
timeout = 5 # seconds
inputs = [sock]
running = 1

#infinite loop - use select() to check for input
#select allows process to respond when input is available
#instead of "blocking" or waiting on input
while running:
    inputready,outputready,exceptready = select.select(inputs,[],[],timeout)

    for s in inputready:

        if s == sock:
            # handle the server socket
            client, address = sock.accept()
            inputs.append(client)
            print('Client connected from', address)

        elif s:
            # handle all other sockets
            data = s.recv(size)
            print('%s: %s' % (s.getpeername(), data.decode().strip('\n')))
            if data:
                print ("data sent -->")
                s.send(data)
            else:
                s.close()
                inputs.remove(s)

sock.close()