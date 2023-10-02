# -*- coding : utf-8 -*-
# @Time: 2023/9/30 15:17
# @Author: yefei.wang
# @File: 1616_checkPalindromeFormation.py


def check(a, b):
    n = len(a)
    i, j = 0, n - 1
    convert = False
    while i < n and j > 0:
        if not convert and a[i] == b[j]:
            i += 1
            j -= 1
        else:
            convert = True
            if b[i] == b[j]:
                i += 1
                j -= 1
            else:
                break

    if i >= j:
        return True


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        x, y = ''.join(list(a)[::-1]), ''.join(list(b)[::-1])
        if check(a, b) or check(b, a) or check(x, y) or check(y, x):
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    a = "pvhmupgqeltozftlmfjjde"
    b = "yjgpzbezspnnpszebzmhvp"
    ret = sol.checkPalindromeFormation(a, b)
    print(ret)
