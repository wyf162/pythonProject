# _*_ coding: utf-8 _*_
# @Time : 2022/4/20 下午9:04 
# @Author : wangyefei
# @File : test-20220420.py
import sys
from typing import List
from collections import defaultdict


def is_unique_sequence(n: int, edges: List):
    adj_tbl = {k:list() for k in range(1, n+1)}
    degree = {k: 0 for k in range(1, n + 1)}
    for s, t in edges:
        adj_tbl[s].append(t)
        degree[t] += 1
    zero_node = list()
    for i in range(1, n + 1):
        if degree[i] == 0:
            zero_node.append(i)
    if len(zero_node) == 1:
        s = zero_node[0]
        visited = set()
        visited.add(s)
        while len(visited) < n:
            if len(adj_tbl[s]) == 1 and adj_tbl[s][0] not in visited:
                s = adj_tbl[s][0]
                visited.add(s)
            else:
                return 'no'
        return 'yes'
    else:
        return 'no'


if __name__ == "__main__":
    sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w+')
    t = int(input())
    for i in range(t):
        m, n = list(map(int, input().split(' ')))
        edges = list()
        for j in range(n):
            edges.append(list(map(int, input().split(' '))))
        print(is_unique_sequence(m, edges))
