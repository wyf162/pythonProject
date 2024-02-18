# -*- coding : utf-8 -*-
# @Time: 2024/2/17 20:56
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


N, Q = MI()
S = input().strip()

A = []
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        A.append(0)
    else:
        A.append(1)

seg_el = 1 << (N.bit_length())  # Segment treeの台の要素数
SEG = [1 << 30] * (2 * seg_el)  # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N - 1):  # Aを対応する箇所へupdate. Aは0-indexedなことに注意.
    SEG[i + seg_el] = A[i]

for i in range(seg_el - 1, 0, -1):  # 親の部分もupdate
    SEG[i] = min(SEG[i * 2], SEG[i * 2 + 1])


def update(n, x, seg_el):  # A[n]をxへ更新
    i = n + seg_el
    SEG[i] = x
    i >>= 1  # 子ノードへ

    while i != 0:
        SEG[i] = min(SEG[i * 2], SEG[i * 2 + 1])
        i >>= 1


def getvalues(l, r):  # 区間[l,r)に関するminを調べる
    L = l + seg_el
    R = r + seg_el
    ANS = 1 << 30

    while L < R:
        if L & 1:
            ANS = min(ANS, SEG[L])
            L += 1

        if R & 1:
            R -= 1
            ANS = min(ANS, SEG[R])
        L >>= 1
        R >>= 1

    return ANS


for queries in range(Q):
    com, l, r = map(int, input().split())

    if com == 2:
        if l == r:
            print("Yes")
            continue
        ANS = getvalues(l - 1, r - 1)

        if ANS == 0:
            print("No")
        else:
            print("Yes")
    else:
        if l - 2 < 0:
            pass
        else:
            A[l - 2] ^= 1
            update(l - 2, A[l - 2], seg_el)

        if r - 1 < len(A):
            A[r - 1] ^= 1
            update(r - 1, A[r - 1], seg_el)


