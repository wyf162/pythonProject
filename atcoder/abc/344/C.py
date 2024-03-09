# -*- coding : utf-8 -*-
# @Time: 2024/3/9 20:06
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

n1 = I()
nums1 = LI()
n2 = I()
nums2 = LI()
n3 = I()
nums3 = LI()
q = I()
queries = LI()

st = set()
for i in range(n1):
    for j in range(n2):
        for k in range(n3):
            st.add(nums1[i] + nums2[j] + nums3[k])

for i in range(q):
    Yn(queries[i] in st)
