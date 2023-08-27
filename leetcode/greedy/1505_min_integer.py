# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 8:56 PM 
# @Author : yefe
# @File : 1505_min_integer


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        class Node:
            def __init__(self, i, j):
                self.l = i
                self.r = j
                self.idx = i
                self.val = [float("inf") for k in range(10)]
                self.lazy = 0
                if i + 1 == j:
                    self.val[int(num[i])] = i
                    return
                mid = (i + j) // 2
                self.left = Node(i, mid)
                self.right = Node(mid, j)
                self.build()

            def get(self):
                if self.l + 1 == self.r:
                    if self.idx is not None:
                        return num[self.idx]
                    return ""
                return self.left.get() + self.right.get()

            def build(self):
                for i in range(10):
                    self.val[i] = min(self.left.val[i], self.right.val[i])

            def pushdown(self):
                self.val = [k + self.lazy for k in self.val]
                if self.l + 1 == self.r:
                    self.lazy = 0
                    return
                self.left.lazy += self.lazy
                self.right.lazy += self.lazy
                self.lazy = 0
                return

            def pop(self, i, n):
                if self.l + 1 == self.r:
                    self.idx = None
                    self.val = [float("inf") for k in range(10)]
                    return
                self.left.lazy += self.lazy
                self.right.lazy += self.lazy
                self.lazy = 0
                if self.left.lazy:
                    self.left.pushdown()
                if self.right.lazy:
                    self.right.pushdown()
                if self.left.val[i] == n:
                    self.left.pop(i, n)
                else:
                    self.left.lazy += 1
                    self.left.pushdown()
                    self.right.pop(i, n)
                self.build()

        l = len(num)
        node = Node(0, l)  # 线段树
        res = ""
        c = 0
        while len(res) < l and k > 0:
            for i in range(10):  # 依次遍历
                if node.val[i] - c <= k:  # 如果可以选择
                    k -= node.val[i] - c  # 更新k
                    node.pop(i, node.val[i])  # 更新线段树
                    res += str(i)
                    break
            c += 1
        if len(res) == l:
            return res
        return res + node.get()
