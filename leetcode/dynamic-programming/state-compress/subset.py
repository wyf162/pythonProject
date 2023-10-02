# -*- coding : utf-8 -*-
# @Time: 2023/9/19 21:25
# @Author: yefei.wang
# @File: subset.py

def get_array(n):
    nums = [i for i in range(1, (1<<n))]
    nums.sort(key=lambda x:bin(x).count('1'))
    return nums


if __name__ == '__main__':
    a = main(3)
    print(a)
