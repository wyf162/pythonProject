# _*_ coding: utf-8 _*_
# @Time : 2022/05/28 12:15 AM 
# @Author : yefe
# @File : 1021_remove_outer_parentheses


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret = ""
        n = len(s)
        stk = [0] * (n + 1)
        for i in range(n):
            if s[i] == ')':
                stk[i + 1] = stk[i] - 1
            else:
                stk[i + 1] = stk[i] + 1
        print(stk)
        skip_flag = True
        for i in range(n):
            if skip_flag:
                skip_flag = False
                continue
            if stk[i + 1] != 0:
                ret += s[i]
            else:
                skip_flag = True

        return ret


if __name__ == '__main__':
    sol = Solution()
    # s = "(()())(())"
    s = "(()())(())(()(()))"
    r = sol.removeOuterParentheses(s)
    print(r)
