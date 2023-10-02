# -*- coding : utf-8 -*-
# @Time: 2022/7/12 21:10
# @Author: yefei.wang
# @File: 424_character_replacement.py
from string import ascii_uppercase


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        n = len(s)
        for ch in ascii_uppercase:
            i = 0
            j = 0
            cnt = 0
            while j < n:
                if s[j] == ch:
                    j += 1
                else:
                    j += 1
                    cnt += 1
                while i < n and cnt > k:
                    if s[i] == ch:
                        i+=1
                    else:
                        cnt -= 1
                        i += 1
                if j - i > ret and cnt <= k:
                    ret = j - i
        return ret


if __name__ == '__main__':
    sol = Solution()
    # s = "ABAB"
    # k = 2
    s = "AABABBA"
    k = 1
    ret = sol.characterReplacement(s, k)
    print(ret)
