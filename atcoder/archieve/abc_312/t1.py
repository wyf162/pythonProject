import sys
import time

sys.setrecursionlimit(10 ** 6)
ans = 0


def dfs(x):
    if x == 0:
        return
    global ans
    ans += x
    dfs(x - 1)


def dfs2(x):
    if x == 0:
        return 0
    return x + dfs2(x - 1)


if __name__ == '__main__':
    N = 3000
    t1 = time.time()
    dfs(N)
    t2 = time.time()
    dfs2(N)
    t3 = time.time()
    print(t2 - t1)
    print(t3 - t2)
