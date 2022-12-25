# -*- coding : utf-8 -*-
# @Time: 2022/6/24 21:14
# @Author: yefei.wang
# @File: gil-00.py

import sys


if __name__ == '__main__':
    a = []
    b = a
    cnt = sys.getrefcount(a)
    print(cnt)
