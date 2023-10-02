# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 1:31 PM 
# @Author : yefe
# @File : 6158_shifting_letters

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n+1)
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end+1] -= 1
            elif direction == 0:
                diff[start] -= 1
                diff[end+1] += 1
        print(diff)

        pres = [0]*(n+1)
        for i in range(n):
            pres[i+1] = pres[i]+diff[i]
        print(pres)

        def get(a: str, k: int) -> str:
            return chr(ord('a') + ((ord(a) - ord('a') + 26 + k) % 26))

        res = ""
        for i, a in enumerate(s):
            res += get(a, pres[i+1])
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    ret = sol.shiftingLetters(s, shifts)
    print(ret)
