# -*- coding : utf-8 -*-
# @Time: 2024/8/18 10:28
# @Author: yefei.wang
# @File: A.py
import bisect


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        pre_zero = [0]
        pre_one = [0]
        for i, c in enumerate(s):
            pre_zero.append(pre_zero[-1] + int(c == '0'))
            pre_one.append(pre_one[-1] + int(c == '1'))

        # print(pre_zero)
        # print(pre_one)
        n = len(s)
        ans = 0
        for i in range(n):
            i1 = bisect.bisect_right(pre_zero, pre_zero[i] + k)
            i2 = bisect.bisect_right(pre_one, pre_one[i] + k)
            ans += max(i2, i1) - i - 1
            # print(i, i1, i2)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "11111"
    k = 1
    ret = sol.countKConstraintSubstrings(s, k)
    print(ret)
