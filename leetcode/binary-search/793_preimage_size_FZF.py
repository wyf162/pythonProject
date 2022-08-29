# _*_ coding: utf-8 _*_
# @Time : 2022/08/28 1:18 PM 
# @Author : yefe
# @File : 793_preimage_size_FZF
import bisect


class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        def zeta(n: int) -> int:
            res = 0
            while n:
                n //= 5
                res += n
            return res

        def nx(k: int) -> int:
            return bisect.bisect_left(range(5*k), k, key=zeta)

        return nx(k+1)-nx(k)


if __name__ == '__main__':
    sol = Solution()
    k = 5
    ret = sol.preimageSizeFZF(k)
    print(ret)
