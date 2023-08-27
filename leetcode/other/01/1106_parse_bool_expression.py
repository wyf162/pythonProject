# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 1:04 PM 
# @Author : yefe
# @File : 1106_parse_bool_expression


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == 'f':
            return False
        elif expression == 't':
            return True
        else:
            if expression[0] == '!':
                return not self.parseBoolExpr(expression[2:-1])
            elif expression[0] == '&':
                ret = True
                for e in self.split_expression(expression[2:-1]):
                    if e==',':
                        continue
                    ret &= self.parseBoolExpr(e)
                return ret
            elif expression[0] == '|':
                ret = False
                for e in self.split_expression(expression[2:-1]):
                    if e==',':
                        continue
                    ret |= self.parseBoolExpr(e)
                return ret

    @staticmethod
    def split_expression(expression):
        result_list = []
        i = 0
        j = 0
        while j < len(expression):
            left = 0
            if expression[j] in "!&|":
                j += 2
                left += 1
            else:
                j += 1
            while left > 0:
                if expression[j] == '(':
                    left += 1
                elif expression[j] == ')':
                    left -= 1
                j += 1
            result_list.append(expression[i:j])
            i = j
        return result_list


if __name__ == '__main__':
    sol = Solution()
    # expression = "&(|(f))"
    expression = "|(&(t,f,t),!(t))"
    ret = sol.parseBoolExpr(expression)
    print(ret)
