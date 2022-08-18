import socket
from gameboard import *


try:
    HOST = input('Enter opponent\'s host name or IP address:\n')  # The remote host
    PORT = int(input('Enter port:\n'))  # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        p1_name = input('Enter your username: ')
        s.sendall(p1_name.encode())
        p2_name = s.recv(1024)
        print(f'Connected to {p2_name}')
        b = Board(s, 'client')
        b.createBoard()
        b.mainLoop()

except Exception:
    try_again = input('Connection failed. Would you like to try again? (Y/N)')
    if try_again == 'N' or try_again == 'n':
        exit()
    else:
        while True:
            HOST = input('Enter opponent\'s host name or IP address:\n')  # The remote host
            PORT = int(input('Enter port:\n'))  # The same port as used by the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                p1_name = input('Enter your username: ')
                s.sendall(p1_name.encode())
                p2_name = s.recv(1024)
                print(f'Connected to {p2_name}')
                b = Board(s, 'client')
                b.createBoard()
                b.mainLoop()
