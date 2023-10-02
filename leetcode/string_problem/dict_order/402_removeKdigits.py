# -*- coding : utf-8 -*-
# @Time: 2023/9/30 10:49
# @Author: yefei.wang
# @File: 402_removeKdigits.py

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        n = len(num)
        m = n - k
        if m == 0:
            return '0'
        for i in range(n):
            while stk and stk[-1] > num[i] and len(stk) + n - i > m:
                stk.pop()
            if len(stk) < m:
                stk.append(num[i])
        rst = ''.join(stk)
        i = 0
        while i < m:
            if rst[i] != 0:
                break
            i += 1
        rst = rst[i:]

        return rst if rst else '0'


if __name__ == '__main__':
    sol = Solution()
    num = "112"
    k = 1
    ret = sol.removeKdigits(num, k)
    print(ret)

# ValueError: Exceeds the limit (4300) for integer string conversion: value has 9001 digits;
# use sys.set_int_max_str_digits() to increase the limit
