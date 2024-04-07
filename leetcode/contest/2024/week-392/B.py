# -*- coding : utf-8 -*-
# @Time: 2024/4/7 10:29
# @Author: yefei.wang
# @File: B.py

from string import ascii_letters


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

        def dist(c1, c2):
            d = abs(ord(c1) - ord(c2)) % 26
            return min(d, 26 - d)

        # for c1 in ascii_letters:
        #     for c2 in ascii_letters:
        #         print(c1, c2, dist(c1, c2))

        t = ''
        for i, c in enumerate(s):
            for tc in ascii_letters:
                if dist(c, tc) <= k:
                    t += tc
                    k -= dist(c, tc)
                    break
        t += s[len(t):]
        return t


if __name__ == '__main__':
    sol = Solution()
    s = "zbbz"
    k = 3
    ret = sol.getSmallestString(s, k)
    print(ret)
