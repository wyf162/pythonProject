# -*- coding : utf-8 -*-
# @Time: 2022/6/11 15:34
# @Author: yefei.wang
# @File: 224_calculate.py
class Solution:
    def calculate(self, s: str) -> int:
        op_stk = []
        num_stk = []

        n = len(s)
        i = 0

        while i < n:
            if '0' <= s[i] <= '9':
                k = 0
                while i < n and '0' <= s[i] <= '9':
                    k *= 10
                    k += int(s[i])
                    i += 1
                num_stk.append(k)
                while op_stk and op_stk[-1] in ['+', '-']:
                    y = num_stk.pop()
                    x = num_stk.pop() if num_stk else 0
                    op = op_stk.pop()
                    z = self.compute(x, y, op)
                    num_stk.append(z)

            elif s[i] in ['+', '-']:
                op_stk.append(s[i])
                i += 1
            elif s[i] == '(':
                op_stk.append(s[i])
                i += 1
            elif s[i] == ')':
                while op_stk and op_stk[-1] in ['+', '-']:
                    y = num_stk.pop()
                    x = num_stk.pop()
                    op = op_stk.pop()
                    z = self.compute(x, y, op)
                    num_stk.append(z)
                op_stk.pop()
                i += 1
                while op_stk and op_stk[-1] in ['+', '-']:
                    y = num_stk.pop()
                    x = num_stk.pop() if num_stk else 0
                    op = op_stk.pop()
                    z = self.compute(x, y, op)
                    num_stk.append(z)
            else:
                i += 1

        print(op_stk)
        print(num_stk)
        res = num_stk[0]
        for i, op in enumerate(op_stk):
            res = self.compute(res, num_stk[i+1], op)
        return res

    @staticmethod
    def compute(x, y, op):
        if op == '-':
            return x - y
        elif op == '+':
            return x + y


if __name__ == '__main__':
    sol = Solution()
    # s = "(1+(4+5+2)-3)+(6+8)"
    # s = "-2+1"
    # s = "2-4-(8+2-6+(8+4-(1)+8-10))"
    s = "1-(-2)"
    # s = "- (3 - (- (4 + 5) ) )"
    ret = sol.calculate(s)
    print(ret)
