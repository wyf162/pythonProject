# -*- coding : utf-8 -*-
# @Time: 2024/5/25 13:33
# @Author: yefei.wang
# @File: demo_scc.py

def find_SCC(graph, n):
    SCC, S, P = [], [], []
    depth = [0] * n

    stack = list(range(n))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


if __name__ == '__main__':
    g = [[1, 2], [0], []]
    scc = find_SCC(g, 3)
    print(scc)
