# -*- coding: utf-8 -*-
# @Time: 2024/5/31 9:28
# @Author: yfwang
# @File: yjsl1025.py
import os, sys, random, threading
# sys.exit() 退出程序
from random import randint, choice, shuffle
# randint(a,b)从[a,b]范围随机选择一个数
# choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
# shuffle(x)将一个可变的序列x中的元素打乱
from copy import deepcopy
from io import BytesIO, IOBase
from types import GeneratorType
from functools import lru_cache, reduce
# reduce(op,迭代对象)
from bisect import bisect_left, bisect_right
# bisect_left(x) 大于等于x的第一个下标
# bisect_right(x) 大于x的第一个下标
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
# accumulate(a)用a序列生成一个累积迭代器，一般list化前面放个[0]做前缀和用
# combinations(a,k)a序列选k个 组合迭代器
# permutations(a,k)a序列选k个 排列迭代器
from heapq import heapify, heappop, heappush
# heapify将列表转为堆
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
from string import ascii_lowercase, ascii_uppercase, digits
# 小写字母，大写字母，十进制数字
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
# ceil向上取整，floor向下取整 ，sqrt开方 ，factorial阶乘
from decimal import Decimal, getcontext
# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
from sys import stdin, stdout, setrecursionlimit

input = lambda: sys.stdin.readline().rstrip("\r\n")
MI = lambda: map(int, input().split())
li = lambda: list(MI())
ii = lambda: int(input())
mod = int(1e9 + 7)  # 998244353
inf = int(1e20)
py = lambda: print("YES")
pn = lambda: print("NO")
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗


class BIT2:
    """区间更新，区间和查询 """
    __slots__ = "size", "_tree1", "_tree2"

    def __init__(self, n: int):
        self.size = n
        self._tree1 = [0] * (n + 1)
        self._tree2 = [0] * (n + 1)

    def add(self, left: int, right: int, delta: int) -> None:
        """闭区间[left, right]加delta"""
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        """闭区间[left, right]的和"""
        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += index & -index

    def _query(self, index: int) -> int:
        if index > self.size:
            index = self.size
        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= index & -index
        return res


def e(a):
    if a == min:
        return 10 ** 15
    if a == max:
        return -10 ** 15


class LcaDoubling:
    def __init__(self, n, graph, root, lcaf):
        """"
        頂点は1-index
        graph[v] = [[u,w],[u,w],...]
        """
        self.lcaf = lcaf
        self.e = e(lcaf)
        # 根からの深さ、距離
        self.depths = [-1] * (n + 1)
        self.distances = [-1] * (n + 1)

        # self.ancestors[k][v]:頂点vから2^k先の親,
        # self.funcs[k][v]:頂点vから2^k先の親までのパス上の1辺の最大（最小）コスト
        prev_ancestors, prev_funcs = self._init_dfs(n, graph, root)
        self.ancestors = [prev_ancestors]
        self.funcs = [prev_funcs]
        max_depth = max(self.depths)
        d = 1
        while d < max_depth:
            next_ancestors = []
            next_funcs = []
            for i in range(len(prev_ancestors)):
                p = prev_ancestors[i]
                dist = prev_funcs[i]
                next_ancestors.append(prev_ancestors[p])
                next_funcs.append(self.lcaf(dist, prev_funcs[p]))
            self.ancestors.append(next_ancestors)
            self.funcs.append(next_funcs)
            d <<= 1
            prev_ancestors = next_ancestors
            prev_funcs = next_funcs

    def _init_dfs(self, n, graph, root):
        que = [(root, -1, 0, 0)]
        direct_ancestors = [-1 for i in range(n + 2)]
        direct_funcs = [self.e for i in range(n + 2)]
        self.depths[root] = 0
        self.distances[root] = 0
        while que:
            crr, pre, dep, dist = que.pop()
            for nxt, w in graph[crr]:
                if nxt == pre:
                    continue
                direct_ancestors[nxt] = crr
                direct_funcs[nxt] = w
                self.depths[nxt] = dep + 1
                self.distances[nxt] = dist + w
                que.append((nxt, crr, dep + 1, dist + w))
        return direct_ancestors, direct_funcs

    def upstream(self, v, k):
        fans = self.e
        b = 0
        while k:
            if k & 1:
                fans = self.lcaf(fans, self.funcs[b][v])
                v = self.ancestors[b][v]
            k >>= 1
            b += 1
        return v, fans

    def get_lca(self, u, v):
        du, dv = self.depths[u], self.depths[v]
        if du > dv:
            u, v = v, u
            du, dv = dv, du
        tu = u
        tv, _ = self.upstream(v, dv - du)
        if tu == tv:
            return tu
        for k in range(du.bit_length())[::-1]:
            mu = self.ancestors[k][tu]
            mv = self.ancestors[k][tv]
            if mu != mv:
                tu = mu
                tv = mv
        lca = self.ancestors[0][tu]
        return lca

    def get_distance(self, u, v):
        lca = self.get_lca(u, v)
        return self.distances[u] + self.distances[v] - 2 * self.distances[lca]

    def get_lcaf(self, u, v):
        lca = self.get_lca(u, v)
        du = self.depths[u] - self.depths[lca]
        dv = self.depths[v] - self.depths[lca]
        _, uans = self.upstream(u, du)
        _, vans = self.upstream(v, dv)
        return self.lcaf(vans, uans)


class HLD:
    def __init__(self, g, root):
        # 无论是点还是dfn还是dep，都从1开始，默认0是无
        n = len(g)
        self.g = g
        self.fa = [0] * (n + 5)  # 父节点，0表示无父节点
        self.size = [1] * (n + 5)  # 子树大小
        self.dep = [0] * (n + 5)  # 深度，根深度为1
        self.son = [0] * (n + 5)  # 重儿子，0表示无儿子
        self.dfn = [0] * (n + 5)  # dfs序，子树终点的dfs序是dfn[i]+size[i]-1
        self.top = [0] * (n + 5)  # 所在重链起点，起点就是自己
        self.rank = [0] * (n + 5)  # dfs序为i的节点编号

        fa = self.fa;
        size = self.size;
        dep = self.dep;
        son = self.son
        dfn = self.dfn;
        top = self.top;
        rank = self.rank
        stk = [[root, 0, 0]]  # node,flag,fa
        dep[root] = 1
        while stk:
            u, flag, father = stk.pop()
            if flag:
                for v in g[u]:
                    if v != father:
                        size[u] += size[v]
                        if son[u] == 0 or size[v] > size[son[u]]:
                            son[u] = v
            else:
                stk.append([u, 1, father])
                for v in g[u]:
                    if v != father:
                        stk.append([v, 0, u])
                        fa[v] = u
                        dep[v] = dep[u] + 1
        stk = [[root, root]]
        tot = 1
        while stk:
            u, tops = stk.pop()
            dfn[u] = tot
            rank[tot] = u
            tot += 1
            top[u] = tops
            if son[u] == 0:
                continue
            for v in g[u]:
                if v != fa[u] and v != son[u]:
                    stk.append([v, v])
            stk.append([son[u], tops])

    def lca(self, u, v):  # 求u和v的最近公共祖先节点
        fa = self.fa;
        size = self.size;
        dep = self.dep;
        son = self.son
        dfn = self.dfn;
        top = self.top;
        rank = self.rank
        while top[u] != top[v]:
            if dep[top[u]] > dep[top[v]]:
                u = fa[top[u]]
            else:
                v = fa[top[v]]
        return v if dep[u] > dep[v] else u

    def dis(self, u, v):
        dep = self.dep
        return dep[u] + dep[v] - 2 * dep[self.lca(u, v)]

    def kth_fa(self, root, k):  # 求root节点的第k个祖先
        fa = self.fa;
        size = self.size;
        dep = self.dep;
        son = self.son
        dfn = self.dfn;
        top = self.top;
        rank = self.rank
        if k >= dep[root]:  # 无第k个祖先返回-1
            return -1
        while True:
            u = top[root]
            if dfn[root] - k >= dfn[u]:
                return rank[dfn[root] - k]
            k -= dfn[root] - dfn[u] + 1
            root = fa[u]

    def route_query(self, u, v):  # 查询u到v简单路径
        fa = self.fa;
        size = self.size;
        dep = self.dep;
        son = self.son
        dfn = self.dfn;
        top = self.top;
        rank = self.rank
        route = []
        while top[u] != top[v]:
            if dep[top[u]] < dep[top[v]]:
                u, v = v, u
            route.append((dfn[top[u]], dfn[u]))
            u = fa[top[u]]
        if dep[u] > dep[v]:
            u, v = v, u
        route.append((dfn[u], dfn[v]))
        return route


class SparseTable:
    def __init__(self, data: list, func=gcd):
        # 稀疏表，O(nlogn)预处理，O(1)查询区间最值/按位与/按位或/gcd/lcm
        # 可以以 O(nlognlong)预处理，O(logn)查询区间lca
        # 下标从0开始
        self.func = func
        self.st = st = [list(data)]
        i, N = 1, len(st[0])
        while 2 * i <= N + 1:
            qz = st[-1]
            st.append([func(qz[j], qz[j + i]) for j in range(N - 2 * i + 1)])
            i <<= 1

    def query(self, begin: int, end: int):  # 查询闭区间[begin, end]的最大值
        lg = (end - begin + 1).bit_length() - 1
        return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])


def bootstrap(f, stack=[]):  # yield
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


class BIT:
    def __init__(self, n):
        self.n = n
        self.max_tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= self.n:
            self.max_tree[idx] = max(self.max_tree[idx], val)
            idx += idx & (-idx)

    def query(self, idx):
        res = 0
        while idx > 0:
            res = max(res, self.max_tree[idx])
            idx -= idx & (-idx)
        return res

