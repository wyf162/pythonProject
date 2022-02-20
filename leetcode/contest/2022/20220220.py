# _*_ coding: utf-8 _*_
# @Time : 2022/2/20 上午10:37 
# @Author : wangyefei
# @File : 20220220.py
from collections import defaultdict, Counter
from math import gcd
from typing import List

from sortedcontainers import SortedDict


class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num + 1):
            cnt = 0
            k = i
            while k > 0:
                cnt += k % 10
                k = k // 10
            if cnt & 1 == 0:
                ans += 1
        return ans

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hst = dict()
        # alphabet = [chr(97+i) for i in range(26)]
        for i in range(len(s)):
            hst[s[i]] = hst.get(s[i], 0) + 1

        sd = SortedDict(hst)
        for k in sd.keys():
            print(k)
        print(sd.keys())

        ans = []
        repeat_tuple = []

        while True:
            flag = False
            for k in reversed(sd.keys()):
                alpha = k
                if repeat_tuple:
                    if repeat_tuple[0] == alpha:
                        if repeat_tuple[1] + 1 > repeatLimit:
                            continue
                        else:
                            repeat_tuple[1] += 1
                            ans.append(alpha)
                            sd[alpha] -= 1
                            self.remove(alpha, sd)
                            flag = True
                            break
                    else:
                        repeat_tuple = [alpha, 1]
                        ans.append(alpha)
                        sd[alpha] -= 1
                        self.remove(alpha, sd)
                        flag = True
                        break
                else:
                    repeat_tuple = [alpha, 1]
                    ans.append(alpha)
                    sd[alpha] -= 1
                    self.remove(alpha, sd)
                    flag = True
                    break

            if not flag:
                break
        return "".join(ans)

    def remove(self, key, sd):
        if sd.get(key) == 0:
            del sd[key]

    def repeat_limited_string(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)

        ans = list()
        for c in range(25, -1, -1):
            ch = chr(ord("a") + c)
            ans.extend([ch] * freq[ch])

        cnt = 1
        # 双指针
        right = 2
        for left in range(1, len(ans)):
            if ans[left - 1] != ans[left]:
                cnt = 1
            else:
                cnt += 1
                if cnt > repeatLimit:
                    right = max(right, left + 1)
                    while right < len(ans) and ans[left] == ans[right]:
                        right += 1

                    if right < len(ans):
                        ans[left], ans[right] = ans[right], ans[left]
                        cnt = 1
                    else:
                        ans = ans[:left]
                        break

        return "".join(ans)

    def cout_airs(self, nums: List[int], k: int) -> int:
        s = 0
        t = 0
        for num in nums:
            if num % k == 0:
                s += 1
            else:
                t += 1
        print(s, t)
        ans = s * t + int(s * (s - 1) / 2)
        return ans

    def coutPairs(self, nums: List[int], k: int) -> int:
        MX = 100001
        divisors = [[] for _ in range(MX)]
        for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
            for j in range(i, MX, i):
                divisors[j].append(i)
        ans = 0
        cnt = defaultdict(int)
        for v in nums:
            ans += cnt[k / gcd(v, k)]
            for d in divisors[v]:
                cnt[d] += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    ans = sol.coutPairs(nums, k)
    print(ans)

    # s = "cczazcc"
    # s = "aaaaaababab"
    # repeatLimit = 2
    # ans = sol.repeatLimitedString(s,repeatLimit)
    # print(ans)
    # ret = sol.countEven(1000)
    # print(ret)
