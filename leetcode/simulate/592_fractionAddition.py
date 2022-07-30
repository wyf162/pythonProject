# -*- coding : utf-8 -*-
# @Time: 2022/7/27 20:06
# @Author: yefei.wang
# @File: 592_fractionAddition.py
from math import gcd


class Fraction:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __iadd__(self, other):
        nb = self.b * other.b
        na = self.a * other.b + other.a * self.b
        return Fraction(na, nb)

    def __str__(self):
        m = gcd(self.a, self.b)
        self.a = self.a // m
        self.b = self.b // m
        return str(self.a) + '/' + str(self.b)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fs = []
        i = 0
        j = 1
        while j < len(expression):
            while j < len(expression) and expression[j] not in '+-':
                j += 1
            a, b = expression[i:j].split('/')
            fs.append(Fraction(int(a), int(b)))
            i = j
            j += 1

        ret = fs[0]
        for i in range(1, len(fs)):
            ret += fs[i]

        return str(ret)


if __name__ == '__main__':
    sol = Solution()
    # expression = "-1/2+1/2"
    expression = "-5/2+10/3+7/9"
    ret = sol.fractionAddition(expression)
    print(ret)
    # print(gcd(0, 4))
