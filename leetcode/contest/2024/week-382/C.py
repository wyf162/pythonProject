# -*- coding : utf-8 -*-
# @Time: 2024/1/28 10:43
# @Author: yefei.wang
# @File: C.py


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        for x in range(1, n + 1):
            if x % 2 == 1:
                ans += m // 2
            else:
                ans += (m + 1) // 2
        return ans


if __name__ == '__main__':
    sol = Solution()
    n, m = 1, 1
    ret = sol.flowerGame(n, m)
    print(ret)
