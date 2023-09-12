#!/usr/bin/env python3
import socket
import time

HOST = 'localhost'
PORT = 12340

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print('\nConnected to server')
        server_time = float(s.recv(1024).decode('utf-8'))
        client_time = time.time()
        print("\nCurrent time : ", client_time)
        offset = server_time - client_time
        s.sendall(str(offset).encode('utf-8'))
        adjusted_time = float(s.recv(1024).decode('utf-8'))
        print("Adjusted time : ", adjusted_time)
        time_diff = adjusted_time - client_time
        print(f'Time difference: {time_diff} seconds')
