# _*_ coding: utf-8 _*_
# @Time : 2022/12/07 11:01 PM 
# @Author : yefe
# @File : server

import os
import socket

host = '127.0.0.1'
port = 65535
s = socket.socket()
s.bind((host, port))
s.listen()

while True:
    conn, addr = s.accept()  # 建立客户端连接
    print('addr:', addr)
    pid = os.fork()
    if pid == 0:
        data = conn.recv(1024)
        print('fork pid', os.getpid())
        print('ppid', os.getppid())
        print(data)
        conn.send(bytes(f"i am server {os.getppid()}", encoding='utf-8'))
        conn.close()
    else:
        data = conn.recv(1024)
        print('pid', os.getpid())
        print(data)
        conn.send(bytes(f"i am server {os.getpid()}", encoding='utf-8'))
        conn.close()



