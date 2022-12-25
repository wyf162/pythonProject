# _*_ coding: utf-8 _*_
# @Time : 10/25/21 7:41 AM 
# @Author : wangyefei
# @File : client.py
import socket
import time

host = socket.gethostname()
port = 12345

t= 0
while True:
    s = socket.socket()
    s.connect((host, port))
    s.send(b'1024')
    time.sleep(1)
    s.close()
    t += 1
    if t>50:
        break
