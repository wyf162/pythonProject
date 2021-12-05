# _*_ coding: utf-8 _*_
# @Time : 2021/11/21 上午10:29 
# @Author : wangyefei
# @File : 20211121.py

from typing import List
import bisect


class Solution1:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur_water = capacity
        cnt = 0
        for idx, plant in enumerate(plants):
            if cur_water >= plant:
                cur_water -= plant
                cnt += 1
            else:
                cur_water = capacity - plant
                cnt = cnt + idx * 2 + 1
        return cnt


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.hs_tbl = dict()
        for i, a in enumerate(arr):
            if a not in self.hs_tbl:
                self.hs_tbl[a] = [i]
            else:
                self.hs_tbl[a].append(i)
        print(self.hs_tbl)

    def query(self, left: int, right: int, value: int) -> int:
        idxs = self.hs_tbl.get(value, [])
        l = bisect.bisect_left(idxs, left)
        r = bisect.bisect_right(idxs, right)
        print(l, r)
        if l == r and idxs[l] == value:
            ans = 1
        else:
            ans = r - l

        return ans


def change(ss, k):
    if not isinstance(ss, str):
        ss = str(ss)
    num = 0
    for s in ss:
        num = num * k + int(s)
    return num


def check(ss):
    if not isinstance(ss, str):
        ss = str(ss)
    return ss == ''.join(reversed(list(ss)))


def next_mirror_number(num, k):
    num = list(str(num))
    n = len(num)
    if n % 2 == 0:
        i = int(n / 2 - 1)
        while i >= 0:
            if int(num[i]) < k - 1:
                break
            i = i - 1
        if i >= 0:
            num[i] = str(int(num[i]) + 1)
            for j in range(i + 1, n - 1 - i):
                num[j] = '0'
            num[n - 1 - i] = num[i]
            return ''.join(num)
        else:
            return '1' + '0' * (n - 1) + '1'
    else:
        i = int(n / 2)
        if int(num[i]) < k - 1:
            num[i] = str(int(num[i]) + 1)
            return ''.join(num)
        else:
            i = i - 1
            while i >= 0:
                if int(num[i]) < k - 1:
                    break
                i = i - 1
            if i >= 0:
                num[i] = str(int(num[i]) + 1)
                for j in range(i + 1, n - 1 - i):
                    num[j] = '0'
                num[n - 1 - i] = num[i]
                return ''.join(num)
            else:
                return '1' + '0' * (n - 1) + '1'


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        cnt = 0
        ans = []
        num = '1'
        while cnt < n:
            print(num)
            while not check(change(num, k)):
                print(num)
                num = next_mirror_number(num, k)
            ans.append(change(num, k))
            cnt += 1
            num = next_mirror_number(num, k)
        print(ans)


if __name__ == "__main__":
    sol = Solution()
    sol.kMirror(7, 17)
    print(next_mirror_number('10201', 7))
    # print(check('545'))
    # ss = "11111"
    # print(change(ss, 3))
    # plants = [3,2,4,2,1]
    # capaticy = 6
    # sol = Solution()
    # print(sol.wateringPlants(plants,capaticy))
    # range_freq_query = RangeFreqQuery([2,2,1,2,2])
    # print(range_freq_query.query(2,4,1))
