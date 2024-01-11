import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log

sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../jury.txt', 'w')
input = lambda: sys.stdin.readline().rstrip('\r\n')
# input = lambda: sys.stdin.buffer.readline()
mi = lambda: map(int, input().split())
li = lambda: list(mi())

for _ in range(int(input())):
    n, m = mi()
    m -= 1
    A = li()
    cum_A = [a for a in A]
    for i in range(1, n):
        cum_A[i] += cum_A[i - 1]

    res = 0

    pq = [-A[m]]
    tmp_m_s = cum_A[m]
    for i in range(m)[::-1]:
        # print(cum_A[i],tmp_m_s,pq)
        while cum_A[i] < tmp_m_s:
            v = heappop(pq)
            v = -v
            tmp_m_s -= 2 * v
            res += 1
        heappush(pq, -A[i])

    cum_A[m] = tmp_m_s
    for i in range(m + 1, n):
        cum_A[i] = cum_A[i - 1] + A[i]

    pq = []
    ms = cum_A[m]
    tmp_S = ms
    for i in range(m + 1, n):
        heappush(pq, A[i])
        tmp_S += A[i]
        while tmp_S < ms:
            v = heappop(pq)
            v *= -1
            tmp_S += 2 * v
            res += 1
    print(res)
