# -*- coding : utf-8 -*-
# @Time: 2024/2/4 11:03
# @Author: yefei.wang
# @File: D.py

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        mx = (len(word) + k - 1) // k
        ans = mx
        n = len(word)
        for i in range(mx):
            suffix = word[(i + 1) * k:n]
            # print(suffix)
            if word.startswith(suffix):
                ans = i + 1
                break
        return ans


if __name__ == '__main__':
    sol = Solution()
    word = "abacaba"
    k = 3
    ret = sol.minimumTimeToInitialState(word, k)
    print(ret)
