# -*- coding : utf-8 -*-
# @Time: 2024/1/6 22:28
# @Author: yefei.wang
# @File: D.py

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, UP: int, s: str) -> int:
        for c in s:
            if int(c) > UP:
                return 0

        start = str(start)
        finish = str(finish)

        def dfs1(i, is_limit, is_num):
            if i == len(start):
                return int(is_num)
            res = 0
            if not is_num:
                if i < len(start) - len(s):
                    res += dfs1(i + 1, False, False)

            down = 0 if (is_num or i == len(finish) - len(s) - 1) else 1
            up = int(start[i]) if is_limit else UP
            if i >= len(start) - len(s):
                k = i - (len(start) - len(s))
                down = int(s[k])
                up = int(s[k])
            for j in range(down, min(up, UP) + 1):
                if is_limit and j > int(start[i]):
                    continue
                res += dfs1(i + 1, is_limit and j == int(start[i]), True)
            return res

        def dfs2(i, is_limit, is_num):
            if i == len(finish):
                return int(is_num)
            res = 0
            if not is_num:
                if i < len(finish) - len(s):
                    res += dfs2(i + 1, False, False)

            down = 0 if (is_num or i == len(finish) - len(s) - 1) else 1
            up = int(finish[i]) if is_limit else UP
            if i >= len(finish) - len(s):
                k = i - (len(finish) - len(s))
                down = int(s[k])
                up = int(s[k])
            for j in range(down, min(up, UP) + 1):
                if is_limit and j > int(finish[i]):
                    continue
                res += dfs2(i + 1, is_limit and j == int(finish[i]), True)
            return res

        x1 = dfs1(0, True, False)
        x2 = dfs2(0, True, False)
        rst = x2 - x1
        # if int(start) < int(s) <= int(finish):
        #     rst += 1
        return rst


if __name__ == '__main__':
    sol = Solution()
    start = 1
    finish = 6000
    limit = 4
    s = "124"
    # start = 15
    # finish = 215
    # limit = 6
    # s = "10"
    # start = 1
    # finish = 971
    # limit = 9
    # s = '41'
    ret = sol.numberOfPowerfulInt(start, finish, limit, s)
    print(ret)
