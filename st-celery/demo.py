# _*_ coding: utf-8 _*_
# @Time : 10/28/21 11:41 PM 
# @Author : wangyefei
# @File : demo.py

from celery import Celery
from celery.utils.log import get_logger

app = Celery('demo', broker='redis://ubuntu:6379/0', result_backend='redis://ubuntu:6379/1')


@app.task
def add(a, b):
    return a+b


if __name__ == "__main__":
    print(app.conf)
    add(1, 1)

