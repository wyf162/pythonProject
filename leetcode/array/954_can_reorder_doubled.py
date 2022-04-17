# _*_ coding: utf-8 _*_
# @Time : 2022/4/1 下午10:09 
# @Author : wangyefei
# @File : 954_can_reorder_doubled.py
from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        print(cnt)
        print(cnt[0])
        print(sorted(cnt, key=abs))
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True


if __name__ == '__main__':
    sol = Solution()
    arr = [-2, -4, 2, 4]
    ret = sol.canReorderDoubled(arr)
    print(ret)
