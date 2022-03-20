# -*- coding : utf-8 -*-
# @Time: 2022/1/13 22:22
# @Author: yefei.wang
# @File: ancient_civilization.py
import sys


def main(n, l, xs):
    s = [0] * l
    for x in xs:
        bs = bin(x)[2:].rjust(l, '0')
        for i in range(l):
            if bs[i] == '1':
                s[i] += 1
    res = ""
    for i in range(l):
        if s[i] > (n >> 1):
            res += "1"
        else:
            res += "0"
    return int(res, 2)


if __name__ == "__main__":
    # data = main(3,5,[18,9,21])
    # print(data)
    sys.stdin = open('input.txt')
    sys.stdout = open('output.txt', 'w+')
    test_case_number = int(sys.stdin.readline())
    for i in range(test_case_number):
        first_line = sys.stdin.readline()
        n, l = first_line.split(' ')
        n, l = int(n), int(l)
        second_line = sys.stdin.readline()
        xs = [int(x) for x in second_line.split(' ')]
        data = main(n, l, xs)
        sys.stdout.write(str(data) + '\n')
        # print(str(data))
