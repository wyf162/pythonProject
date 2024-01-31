import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
from sys import stdin

n = int(stdin.readline())
g = [[] for i in range(n)]
for _ in range(n - 1):
    x, y = map(int, stdin.readline().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)
subtree_size = [0] * n
stack = [[-1, 0, 0]]
ans = []
while stack:
    par, ver, state = stack.pop()
    if state == 0:
        stack.append([par, ver, 1])
        for to in g[ver]:
            if to != par:
                stack.append([ver, to, 0])
    else:
        if len(g[ver]) == 1:
            subtree_size[ver] = 1
        else:
            cnt = 0
            tmp = []
            for to in g[ver]:
                if to != par:
                    cnt += subtree_size[to]
                    tmp.append(subtree_size[to])
            tmp.append(n - cnt - 1)
            local = [0] * (n + 1)
            local[0] = 1
            for x in tmp:
                for i in range(n - x, -1, -1):
                    if local[i] == 1:
                        local[i + x] = 1
                        if x + i != 0 and n - 1 - (x + i) != 0:
                            ans.append(x + i)
            subtree_size[ver] = cnt + 1
ans = sorted(list(set(ans)))
print(len(ans))
for x in ans:
    print(x, n - 1 - x)
