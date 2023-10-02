# -*- coding : utf-8 -*-
# @Time: 2022/8/7 16:34
# @Author: yefei.wang
# @File: 1147_longest_decomposition.py

class Solution:
    def longestDecomposition2(self, text: str) -> int:
        n = len(text)
        res = 0
        l0, l = 0, 0
        r = n - 1
        while l <= r:
            while text[l] != text[r]:
                l += 1
            if l == r:
                res += 1
                break
            elif l < r:
                word_len = l - l0 + 1
                if text[l0:l + 1] == text[r - word_len + 1:r + 1]:
                    res += 2
                    l += 1
                    l0 = l
                    r -= word_len
                else:
                    l += 1
            elif l > r:
                break
        return res

    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        for i in range((n >> 1)):
            if text[:i+1] == text[-(i+1):]:
                return 2 + self.longestDecomposition(text[i+1:-(i+1)])
        return 1 if text else 0


if __name__ == '__main__':
    sol = Solution()
    # text = "aba"
    text = "elvtoelvto"
    ret = sol.longestDecomposition(text)
    print(ret)
