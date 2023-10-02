# -*- coding : utf-8 -*-
# @Time: 2023/9/30 19:23
# @Author: yefei.wang
# @File: 2663.py

from string import ascii_lowercase


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        alphabet = ascii_lowercase[:k]

        def next_string(s, k):
            ss = list(s)
            carry = 1
            for i in range(len(ss)-1, -1, -1):
                idx = ord(ss[i]) - ord('a')
                carry, idx = divmod(idx+carry, k)
                ss[i] = alphabet[idx]
            if carry:
                ss.insert(0, 'a')
            return ''.join(ss)

        def check(s):
            n = len(s)
            for i in range(1, n):
                if s[i] == s[i-1]:
                    return False
            for i in range(2, n):
                if s[i] == s[i-2]:
                    return False
            return True

        t = next_string(s, k)
        while len(t) == len(s):
            if check(t):
                return t
            t = next_string(t, k)
        return ''


if __name__ == '__main__':
    sol = Solution()
    s = "abcz"
    k = 26
    ret = sol.smallestBeautifulString(s, k)
    print(ret)
