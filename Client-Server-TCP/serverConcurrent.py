from multiprocessing import connection
import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1159
ThreadCount = 0

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "Data.csv")
print(file_path)


try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waitiing for a Connection..')
ServerSocket.listen(5)
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
while True:
    data = connection.recv(2048)
    print('Received from client :' + str(ThreadCount) + data.decode())
    Inputs = input('Server Says: ')
    if not data:
        break
connection.sendall(Inputs.encode())
connection.close()
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()

