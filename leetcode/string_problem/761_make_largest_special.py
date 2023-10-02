# -*- coding : utf-8 -*-
# @Time: 2022/8/8 19:43
# @Author: yefei.wang
# @File: 761_make_largest_special.py


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cur, last = 0, 0
        ret = []
        for i in range(len(s)):
            cur += 1 if s[i] == '1' else -1
            if cur == 0:
                ret.append('1' + self.makeLargestSpecial(s[last + 1: i]) + '0')
                last = i + 1
        return ''.join(sorted(ret, reverse=True))


if __name__ == '__main__':
    sol = Solution()
    s = "11011000"
    ret = sol.makeLargestSpecial(s)
    print(ret)
