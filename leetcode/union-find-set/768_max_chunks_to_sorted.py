# _*_ coding: utf-8 _*_
# @Time : 2022/08/13 9:50 AM 
# @Author : yefe
# @File : 768_max_chunks_to_sorted
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        unorder_array = arr
        order_aray = sorted(arr)

        ui = 0  # 无序数组的索引
        oi = 0  # 有序数组的索引
        ans = 0
        m = -1  # 用于记录区间的最大值
        while ui < n and oi < n:
            m = unorder_array[ui]
            while ui < n and unorder_array[ui] != order_aray[oi]:
                if unorder_array[ui]>m:
                    m = unorder_array[ui]
                ui += 1
            while ui < n and unorder_array[ui] < m:
                ui += 1
            if ui==oi:
                ui += 1
            ans += 1

            oi = ui
        return ans


if __name__ == '__main__':
    sol = Solution()
    # arr = [5, 4, 3, 2, 1]
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 1, 3, 4, 4]
    # arr = [5, 3, 2, 5, 5]
    # arr = [4, 2, 2, 1, 1]
    # arr = [0, 0, 1, 1, 1]
    arr = [0,3,0,3,2]
    ret = sol.maxChunksToSorted(arr)
    print(ret)
