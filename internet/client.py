# _*_ coding: utf-8 _*_
# @Time : 10/25/21 7:41 AM 
# @Author : wangyefei
# @File : client.py
import socket

s = socket.socket()
host = socket.gethostname()
port = 8888

s.connect((host, port))
s.send(b'1024')
s.close()
