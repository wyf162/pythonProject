# -*- coding : utf-8 -*-
# @Time: 2022/8/10 22:14
# @Author: yefei.wang
# @File: 640_solve_equation.py
class Solution:
    def solveEquation(self, equation: str) -> str:

        def simplify(expression):
            x, v = 0, 0
            sign = 1
            i = 0
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression == '+':
                sign = 1
                i += 1

            while i < len(expression):
                if expression[i].isdigit():
                    t = int(expression[i])
                    i += 1
                    while i < len(expression) and expression[i].isdigit():
                        t = t * 10 + int(expression[i])
                        i += 1
                    if i < len(expression) and expression[i] == 'x':
                        x += t * sign
                        i += 1
                    else:
                        v += t * sign
                    if i >= len(expression):
                        break
                    if expression[i] == '-':
                        sign = -1
                    else:
                        sign = 1

                elif expression[i] == 'x':
                    x += sign
                    i += 1
                    if i >= len(expression):
                        break
                    if expression[i] == '-':
                        sign = -1
                    else:
                        sign = 1
                    i += 1
                else:
                    i += 1
            return x, v

        left, right = equation.split('=')
        lx, lv = simplify(left)
        rx, rv = simplify(right)

        x = lx - rx
        v = rv - lv

        if x == 0 and v != 0:
            return "No solution"
        elif x == 0:
            return "Infinite solutions"
        else:
            return f"x={v // x}"


if __name__ == '__main__':
    sol = Solution()
    # equation = "x+5-3+x=6+x-2"
    equation = "x=x+2"
    ret = sol.solveEquation(equation)
    print(ret)
