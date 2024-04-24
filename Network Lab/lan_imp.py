# CREATING THE SERVER

import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set a port number for the server to listen on
port = 12345

# bind the socket to a specific address and port
server_socket.bind((host, port))

# listen for incoming connections
server_socket.listen(5)

# wait for a connection to be established
client_socket, addr = server_socket.accept()

print('Got connection from', addr)

# --------------------------------------------------------------------

# CREATING THE CLIENT

import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set a port number for the client to connect to
port = 12345

# connect to the server
client_socket.connect((host, port))

# send data to the server
client_socket.send(b'Hello, server!')

# receive data from the server
data = client_socket.recv(1024)

print('Received:', repr(data))

# --------------------------------------------------------------------

# USE OF THREADING

# import socket
# import threading

# # create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # get local machine name
# host = socket.gethostname()

# # set a port number for the server to listen on
# port = 12345

# # bind the socket to a specific address and port
# server_socket.bind((host, port))

# # listen for incoming connections
# server_socket.listen(5)

# def handle_client(client_socket, addr):
#     while True:
#         # receive data from the client
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         print('Received:', repr(data), 'from', addr)

#         # send data back to the client
#         client_socket.send(data)

#     # close the client socket
#     client_socket.close()
#     print('Connection closed by', addr)

# while True:
#     # wait for a connection to be established
#     client_socket, addr = server_socket.accept()

#     # create a new thread to handle the connection
#     client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
#     client_thread.start()