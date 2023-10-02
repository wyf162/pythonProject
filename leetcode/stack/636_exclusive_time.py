# -*- coding : utf-8 -*-
# @Time: 2022/8/7 10:23
# @Author: yefei.wang
# @File: 636_exclusive_time.py
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stk = []
        prev = 0
        prev_tag = ''
        for log in logs:
            func, flag, ts = log.split(':')
            func, ts = int(func), int(ts)
            if flag == 'start':
                if stk:
                    ans[stk[-1]] += ts - prev + (-1 if prev_tag == 'end' else 0)
                stk.append(func)
                prev = ts
                prev_tag = flag
            elif flag == 'end':
                ans[func] += ts - prev + (1 if prev_tag == 'start' else 0)
                prev = ts
                prev_tag = flag
                stk.pop()
        return ans


if __name__ == '__main__':
    sol = Solution()
    # n = 2
    # logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    n = 1
    logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    ret = sol.exclusiveTime(n, logs)
    print(ret)
