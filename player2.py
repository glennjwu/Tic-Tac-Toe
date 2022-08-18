import socket
from gameboard import *

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Waiting for connection...')
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    print('Waiting for opponent...')
    p1_name = conn.recv(1024)
    print(f'Connecting to {p1_name}')
    conn.sendall(b'player2')
    b = Board(conn, 'server')
    b.createBoard()
    b.mainLoop()

