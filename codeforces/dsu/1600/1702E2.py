import sys

import math
from heapq import heapify, heappush, heappop
from bisect import bisect_right, bisect_left
from itertools import *
from collections import *

input = lambda: sys.stdin.readline().rstrip()
inf = float('inf')


def error(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end, file=sys.stderr)


# sys.setrecursionlimit(10**5)

#  -----------------------  #

def main():
    n = int(input())
    G = [[] for _ in range(n)]
    ab = [list(map(int, input().split())) for _ in range(n)]
    for a, b in ab:
        a -= 1
        b -= 1
        if a == b:
            return 'NO'
        G[a].append(b)
        G[b].append(a)
    for i in range(n):
        if len(G[i]) != 2:
            return 'NO'

    col = [0] * n

    for i in range(n):
        if col[i] == 0:
            col[i] = 1
            todo = deque([i])
            while todo:
                v = todo.popleft()
                for x in G[v]:
                    if col[x] == 0:
                        col[x] = -col[v]
                        todo.append(x)
                    elif col[x] == -col[v]:
                        continue
                    else:
                        return 'NO'
    return 'YES' if col.count(1) == n // 2 else 'NO'


print('\n'.join(str(main()) for _ in range(int(input()))))
