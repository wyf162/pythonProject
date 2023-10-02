# -*- coding : utf-8 -*-
# @Time: 2023/8/27 16:14
# @Author: yefei.wang
# @File: d.py
# import copy
# import sys
#
# sys.stdin = open('input.txt', 'r')


def matrix_cascade(n, mtx):
    ans = 0
    st = [0] * (n + 1)
    en = [0] * (n + 1)
    for i in range(n):
        st[0] += st[1]
        for k in range(1, n):
            st[k] = st[k+1]
        st[n-1] = 0

        for k in range(n, 0, -1):
            en[k] = en[k-1]
        tmp = []
        cnt = 0
        for j in range(n):
            cnt += st[j] - en[j]
            if (mtx[i][j] + cnt) % 2:
                ans += 1
                tmp.append(j)
        for k in tmp:
            st[k] += 1
            en[k+1] += 1

    print(ans)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n = int(input())
        mtx = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            s = input()
            for j in range(n):
                mtx[i][j] = int(s[j])
        matrix_cascade(n, mtx)


if __name__ == '__main__':
    main()
