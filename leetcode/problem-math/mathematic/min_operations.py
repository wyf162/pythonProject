# _*_ coding: utf-8 _*_
# @Time : 2022/12/03 11:22 AM 
# @Author : yefe
# @File : min_operations

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(box) for box in boxes]
        pres = [0]
        for i, box in enumerate(boxes):
            pres.append(pres[-1]+box)
        n = len(boxes)
        ans = [0] * n

        ans[0] = sum(i*box for i, box in enumerate(boxes))
        for i in range(1, n):
            ans[i] = ans[i-1] + pres[i] - (pres[-1]-pres[i+1]) - boxes[i]

        return ans


if __name__ == '__main__':
    sol = Solution()
    boxes = "110"
    ret = sol.minOperations(boxes)
    print(ret)
