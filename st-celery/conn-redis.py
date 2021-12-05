# _*_ coding: utf-8 _*_
# @Time : 10/28/21 11:50 PM 
# @Author : wangyefei
# @File : conn-redis.py
import redis

host = 'ubuntu'
port = 6379

r = redis.Redis(host, port)

r.set('w', 'y')
print(r.get('w'))