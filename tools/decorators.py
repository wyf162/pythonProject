# -*- coding : utf-8 -*-
# @Time: 2022/1/2 0:24
# @Author: yefei.wang
# @File: decorators.py
import time


def print_run_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        data = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__} time cost {t2-t1}s")
        return data
    return wrapper


