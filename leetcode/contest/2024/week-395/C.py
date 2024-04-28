# -*- coding : utf-8 -*-
# @Time: 2024/4/28 10:40
# @Author: yefei.wang
# @File: C.py

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        s1 = list(bin(x)[2:])
        s2 = list(bin(n - 1)[2:])
        s1.reverse()
        s2.reverse()

        n1 = len(s1)
        n2 = len(s2)
        i2 = 0
        for i1 in range(n1):
            if i2 >= n2:
                break
            if s1[i1] == '0':
                s1[i1] = s2[i2]
                i2 += 1
        s1 += s2[i2:]
        s1.reverse()
        ret = int(''.join(s1), 2)
        return ret


if __name__ == '__main__':
    sol = Solution()
    n = 2
    x = 7
    ret = sol.minEnd(n, x)
    print(ret)

