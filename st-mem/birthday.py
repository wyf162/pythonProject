# -*- coding : utf-8 -*-
# @Time: 2021/12/26 22:11
# @Author: yefei.wang
# @File: birthday.py

from datetime import datetime

if __name__ == "__main__":
    days = datetime(2021, 12, 31) - datetime(1997, 12, 31)
    print(days)
