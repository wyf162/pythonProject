# _*_ coding: utf-8 _*_
# @Time : 2022/04/30 5:02 PM 
# @Author : yefe
# @File : 17008_best_seq_at_index
import bisect
from typing import List


class Solution:
    def bestSeqAtIndex2(self, height: List[int], weight: List[int]) -> int:
        stack = []
        for h, w in sorted([h, -w] for h, w in zip(height, weight)):
            w = -w
            if not stack or stack[-1][1] < w:
                stack.append([h, w])
            else:
                idx = bisect.bisect_left([s[1] for s in stack], w)
                stack[idx][1] = w
            print(stack)
        return len(stack)

    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        stack = []
        ret = len(stack)
        for h, w in sorted([h, -w] for h, w in zip(height, weight)):
            w = -w
            if not stack or stack[-1][1] < w:
                stack.append((h, w))
            else:
                while stack and stack[-1][1] > w:
                    stack.pop()
                stack.append((h,w))
            ret = max(ret, len(stack))
            print(stack)
        return ret


if __name__ == '__main__':
    sol = Solution()
    # height = [65, 70, 56, 75, 60, 68]
    # weight = [100, 150, 90, 190, 95, 110]
    height = [8378, 8535, 8998, 3766, 648, 6184, 5506, 5648, 3907, 6773]
    weight = [9644, 849, 3232, 3259, 5229, 314, 5593, 9600, 6695, 4340]
    ret = sol.bestSeqAtIndex(height, weight)
    print(ret)
    ret = sol.bestSeqAtIndex2(height, weight)
    print(ret)
