# _*_ coding: utf-8 _*_
# @Time : 2022/4/10 上午10:29 
# @Author : wangyefei
# @File : week-288-20220410.py
from typing import List
import heapq
import bisect


class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(map(int, list(str(num))))
        flag = [0] * len(nums)
        odd_nums = list()
        event_nums = list()
        for idx, num in enumerate(nums):
            if num % 2 == 1:
                flag[idx] = 1
                odd_nums.append(num)
            else:
                flag[idx] = 0
                event_nums.append(num)
        odd_nums.sort()
        event_nums.sort()
        ret = 0
        for i in range(len(nums)):
            if flag[i] == 1:
                ret = ret * 10 + odd_nums.pop()
            else:
                ret = ret * 10 + event_nums.pop()
        return ret

    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split('+')
        m, n = len(a), len(b)
        ret = int(a) + int(b)
        ans = '(' + expression + ')'
        for i in range(0, m):
            for j in range(1, n + 1):
                c, d, e, f = int(a[:i] or 1), int(a[i:]), int(b[:j]), int(b[j:] or 1)
                print(c, d, e, f)
                if ret > c * (d + e) * f:
                    ret = c * (d + e) * f
                    if j == n:
                        ans = a[:i] + '(' + a[i:] + '+' + b[:j] + ')'
                    else:
                        ans = a[:i] + '(' + a[i:] + '+' + b[:j] + ')' + b[j:]

        return ans

    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            num = heapq.heappop(nums)
            print(num)
            heapq.heappush(nums, num + 1)
            k -= 1
        print(nums)
        ret = 1
        for num in nums:
            ret = ret * num
            ret = ret % 1000000007
        return ret

    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()
        idx1 = bisect.bisect_left(flowers, target)

        # 前缀和数组
        pre = [0] * (idx1+1)
        for i in range(idx1):
            pre[i+1] = pre[i] + flowers[i]

        if target * idx1 - pre[-1] <= newFlowers:
            ret = n*full
        else:
            ret = 0

        idx2 = idx1
        i = 0
        while i < idx1:
            if target * (idx1 - i - 1) - (pre[-1] - pre[i-1]) <= newFlowers:
                idx2 = i
                break
            i += 1

        for i in range(idx2, idx1):
            full_num = n - i
            k = newFlowers - (target * (idx1-i) - (pre[-1] - pre[i]))
            partial_val = self.min_max(flowers[:i], pre[:i+1], k, target)
            tmp = full_num * full + partial_val * partial
            ret = max(ret, tmp)
        return ret

    def min_max(self, nums, pres, k, target):
        #
        if not nums:
            return 0
        l = 0
        r = target-1
        while l <= r:
            m = (l + r) >> 1
            idx = bisect.bisect_right(nums, m)
            if m * idx - pres[idx] <= k:
                l += 1
            else:
                r -= 1
        return r


if __name__ == '__main__':
    sol = Solution()
    flowers = [1, 3, 1, 1]
    newFlowers = 7
    target = 6
    full = 12
    partial = 1
    # flowers = [2, 4, 5, 3]
    # newFlowers = 10
    # target = 5
    # full = 2
    # partial = 6
    ret = sol.maximumBeauty(flowers, newFlowers, target, full, partial)
    print(ret)


    # nums = [2, 3, 4, 5]
    # pres = [0, 2, 5, 9, 14]
    # ret = sol.min_max(nums, pres, 3, 6)
    # print(ret)

    # nums = [6, 3, 3, 2]
    # k = 2
    # ret = sol.maximumProduct(nums, k)
    # print(ret)

    # expression = "247+38"
    # expression = "12+34"
    # expression = "5+22"
    # ret = sol.minimizeResult(expression)
    # print(ret)

    # num = 1234
    # num = 699999998
    # ret = sol.largestInteger(num)
    # print(ret)
