# -*- coding : utf-8 -*-
# @Time: 2024/7/28 10:42
# @Author: yefei.wang
# @File: C.py

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pre_sum_zero = [0]
        pre_sum_one = [0]
        for i, c in enumerate(s):
            pre_sum_zero.append(pre_sum_zero[-1] + int(c == '0'))
            pre_sum_one.append(pre_sum_one[-1] + int(c == '1'))

        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n, 1):
                c0 = pre_sum_zero[j + 1] - pre_sum_zero[i]
                c1 = pre_sum_one[j + 1] - pre_sum_one[i]
                # print(i, j, c0, c1)
                if c0 > 200:
                    break
                if c1 >= (n - j + c0) * (n - j + c0):
                    ans += n - j + 1
                    break

                if c0 * c0 <= c1:
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "1" * 40000
    ret = sol.numberOfSubstrings(s)
    print(ret)
