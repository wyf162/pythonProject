# -*- coding: utf-8 -*-
# @Time: 2024/5/28 15:00
# @Author: yfwang
# @File: 3163.py

class Solution:
    def compressedString(self, word: str) -> str:
        ret = ''
        n = len(word)
        c = word[0]
        k = 1
        for i in range(1, n):
            if word[i] == c and k < 9:
                k += 1
            else:
                ret += str(k) + c
                c = word[i]
                k = 1
        ret += str(k) + c
        return ret


if __name__ == '__main__':
    sol = Solution()
    word = 'abcde'
    ret = sol.compressedString(word)
    print(ret)