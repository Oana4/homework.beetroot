import socket

my_socket = socket.socket()

port = 22344

with my_socket as s:
    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    # receive data from the server and decoding to get the string.
    print(s.recv(1024).decode())

