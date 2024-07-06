# -*- coding : utf-8 -*-
# @Time: 2024/7/5 23:53
# @Author: yefei.wang
# @File: find_cycle.py


g = [[1, 2], [0, 2], [1, 0, 3], [2]]
vis = [0] * 4
parent = [-1] * 4
in_cycle = [0] * 4


def dfs(x):
    vis[x] = 1
    for y in g[x]:
        if vis[y] == 1 and y != parent[x]:
            tmp = x
            print("cycle: ", end="")
            while tmp != y:
                in_cycle[tmp] = 1
                print(tmp, '->', end='')
                tmp = parent[tmp]
            print(tmp)
            in_cycle[tmp] = 1
        elif vis[y] == 0:
            parent[y] = x
            dfs(y)
    vis[x] = 2


def dfs2(x):
    stk = [(x, 0)]
    while stk:
        x, state = stk.pop()
        if state == 0:
            vis[x] = 1
            stk.append((x, 1))
            for y in g[x]:
                if vis[y] == 1 and y != parent[x]:
                    tmp = x
                    print("cycle: ", end="")
                    while tmp != y:
                        in_cycle[tmp] = 1
                        print(tmp, '->', end='')
                        tmp = parent[tmp]
                    print(tmp)
                    in_cycle[tmp] = 1
                elif vis[y] == 0:
                    parent[y] = x
                    stk.append((y, 0))
        else:
            vis[x] = 2


dfs2(0)
print(vis)
print(in_cycle)
