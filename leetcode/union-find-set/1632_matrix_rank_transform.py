# _*_ coding: utf-8 _*_
# @Time : 2023/01/26 2:36 PM 
# @Author : yefe
# @File : 1632_matrix_rank_transform

from typing import List
from collections import defaultdict, Counter, deque


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        uf = UnionFind(m, n)
        for i, row in enumerate(matrix):
            num2indexList = defaultdict(list)
            for j, num in enumerate(row):
                num2indexList[num].append([i, j])
            for indexList in num2indexList.values():
                i1, j1 = indexList[0]
                for k in range(1, len(indexList)):
                    i2, j2 = indexList[k]
                    uf.union(i1, j1, i2, j2)
        for j in range(n):
            num2indexList = defaultdict(list)
            for i in range(m):
                num2indexList[matrix[i][j]].append([i, j])
            for indexList in num2indexList.values():
                i1, j1 = indexList[0]
                for k in range(1, len(indexList)):
                    i2, j2 = indexList[k]
                    uf.union(i1, j1, i2, j2)

        degree = Counter()
        adj = defaultdict(list)
        for i, row in enumerate(matrix):
            num2index = {}
            for j, num in enumerate(row):
                num2index[num] = (i, j)
            sortedArray = sorted(num2index.keys())
            for k in range(1, len(sortedArray)):
                i1, j1 = num2index[sortedArray[k - 1]]
                i2, j2 = num2index[sortedArray[k]]
                ri1, rj1 = uf.find(i1, j1)
                ri2, rj2 = uf.find(i2, j2)
                degree[(ri2, rj2)] += 1
                adj[(ri1, rj1)].append([ri2, rj2])
        for j in range(n):
            num2index = {}
            for i in range(m):
                num = matrix[i][j]
                num2index[num] = (i, j)
            sortedArray = sorted(num2index.keys())
            for k in range(1, len(sortedArray)):
                i1, j1 = num2index[sortedArray[k - 1]]
                i2, j2 = num2index[sortedArray[k]]
                ri1, rj1 = uf.find(i1, j1)
                ri2, rj2 = uf.find(i2, j2)
                degree[(ri2, rj2)] += 1
                adj[(ri1, rj1)].append([ri2, rj2])

        rootSet = set()
        ranks = {}
        for i in range(m):
            for j in range(n):
                ri, rj = uf.find(i, j)
                rootSet.add((ri, rj))
                ranks[(ri, rj)] = 1
        q = deque([[i, j] for i, j in rootSet if degree[(i, j)] == 0])
        while q:
            i, j = q.popleft()
            for ui, uj in adj[(i, j)]:
                degree[(ui, uj)] -= 1
                if degree[(ui, uj)] == 0:
                    q.append([ui, uj])
                ranks[(ui, uj)] = max(ranks[(ui, uj)], ranks[(i, j)] + 1)
        res = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ri, rj = uf.find(i, j)
                res[i][j] = ranks[(ri, rj)]
        return res


class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.root = [[[i, j] for j in range(n)] for i in range(m)]
        self.size = [[1] * n for _ in range(m)]

    def find(self, i, j):
        ri, rj = self.root[i][j]
        if [ri, rj] == [i, j]:
            return [i, j]
        self.root[i][j] = self.find(ri, rj)
        return self.root[i][j]

    def union(self, i1, j1, i2, j2):
        ri1, rj1 = self.find(i1, j1)
        ri2, rj2 = self.find(i2, j2)
        if [ri1, rj1] != [ri2, rj2]:
            if self.size[ri1][rj1] >= self.size[ri2][rj2]:
                self.root[ri2][rj2] = [ri1, rj1]
                self.size[ri1][rj1] += self.size[ri2][rj2]
            else:
                self.root[ri1][rj1] = [ri2, rj2]
                self.size[ri2][rj2] += self.size[ri1][rj1]
