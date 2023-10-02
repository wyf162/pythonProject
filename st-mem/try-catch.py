# -*- coding : utf-8 -*-
# @Time: 2021/12/12 20:11
# @Author: yefei.wang
# @File: try-catch.py

def test_01():
    try:
        y = 1/0
        print("try")
    except Exception as e:
        print("exception")
    else:
        print("else")
    finally:
        print("finally")


if __name__ == "__main__":
    test_01()
