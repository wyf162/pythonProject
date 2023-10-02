# -*- coding : utf-8 -*-
# @Time: 2023/8/27 10:26
# @Author: yefei.wang
# @File: minimumPossibleSum.py


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:

        cnt = 0
        i = 1
        s = set()
        while cnt < n:
            if target - i not in s:
                s.add(i)
                cnt += 1
            i += 1
        return sum(s)


if __name__ == '__main__':
    sol = Solution()
    n = 3
    target = 3
    ret = sol.minimumPossibleSum(n, target)
    print(ret)
