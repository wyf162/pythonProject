# _*_ coding: utf-8 _*_
# @Time : 2022/05/28 10:49 PM 
# @Author : yefe
# @File : 10011_BookMyShow
from typing import List
import bisect


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (n * 4)
        self.sum = [0] * (n * 4)

    # 将 idx 上的元素值增加 val
    def add(self, o: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if idx <= m: self.add(o * 2, l, m, idx, val)
        else: self.add(o * 2 + 1, m + 1, r, idx, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 返回区间 [L,R] 内的元素和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int):
        if L <= l and r <= R: return self.sum[o]
        sum = 0
        m = (l + r) // 2
        if L <= m: sum += self.query_sum(o * 2, l, m, L, R)
        if R > m: sum += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return sum

    # 返回区间 [1,R] 中 <= val 的最靠左的位置，不存在时返回 0
    def index(self, o: int, l: int, r: int, R: int, val: int):
        if self.min[o] > val: return 0  # 说明整个区间的元素值都大于 val
        if l == r: return l
        m = (l + r) // 2
        if self.min[o * 2] <= val: return self.index(o * 2, l, m, R, val)  # 看看左半部分
        if m < R: return self.index(o * 2 + 1, m + 1, r, R, val)  # 看看右半部分
        return 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.index(1, 1, self.n, maxRow + 1, self.m - k)
        if i == 0: return []
        seats = self.query_sum(1, 1, self.n, i, i)
        self.add(1, 1, self.n, i, k)  # 占据 k 个座位
        return [i - 1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        if (maxRow + 1) * self.m - self.query_sum(1, 1, self.n, 1, maxRow + 1) < k:
            return False  # 剩余座位不足 k 个
        i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)  # 从第一个没有坐满的排开始占座
        while True:
            left_seats = self.m - self.query_sum(1, 1, self.n, i, i)
            if k <= left_seats:  # 剩余人数不够坐后面的排
                self.add(1, 1, self.n, i, k)
                return True
            k -= left_seats
            self.add(1, 1, self.n, i, left_seats)
            i += 1


if __name__ == '__main__':
    # cmds = ["BookMyShow", "gather", "scatter", "gather", "gather", "gather"]
    # parms = [[5, 9], [10, 1], [3, 3], [9, 1], [10, 2], [2, 0]]
    cmds = ["BookMyShow", "scatter", "gather", "gather", "gather"]
    parms = [[5, 3], [3, 2], [10, 2], [1, 1], [9, 4]]
    # [null,true,[],[1,0],[]]
    n = len(cmds)
    my_book = BookMyShow(*parms[0])
    for i in range(1, n):
        if cmds[i] == 'gather':
            ret = my_book.gather(*parms[i])
            print(ret)
        elif cmds[i] == 'scatter':
            ret = my_book.scatter(*parms[i])
            print(ret)
    # my_book = BookMyShow(2, 5)
    # ret = my_book.gather(4, 0)
    # print(ret)
    # ret = my_book.gather(2, 0)
    # print(ret)
    # ret = my_book.scatter(5, 1)
    # print(ret)
    # ret = my_book.scatter(5, 1)
    # print(ret)
