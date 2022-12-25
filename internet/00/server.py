# _*_ coding: utf-8 _*_
# @Time : 10/26/21 7:26 AM 
# @Author : wangyefei
# @File : server.py
import socket  # 导入 socket 模块
import os

print('pid', os.getpid())

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
print('host:', host)
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    conn, addr = s.accept()  # 建立客户端连接
    print('addr:', addr)
    pid = os.fork()
    if pid == 0:
        data = conn.recv(1024)
        print('fork pid', os.getpid())
        print('ppid', os.getppid())
        print(data)
        conn.close()
    else:
        conn.close()

