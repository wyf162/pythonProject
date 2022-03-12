# _*_ coding: utf-8 _*_
# @Time : 2022/2/27 下午3:04 
# @Author : wangyefei
# @File : 39_combinationSum.py
from typing import List
from collections import Counter


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = list()

        def backtrack(cands, s, idx):
            if s > target:
                return
            elif s == target:
                self.ans.append(cands)
            else:
                for idx in range(idx, len(candidates)):
                    backtrack(cands + [candidates[idx]], s + candidates[idx], idx)

        backtrack([], 0, 0)
        return self.ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = list()
        candidates = dict(Counter(candidates))
        candidates = [(x, y) for x, y in candidates.items()]
        print(candidates)

        def backtrack(cands, s, idx):
            if s > target:
                return
            elif s == target:
                self.ans.append(cands)
            else:
                if idx < len(candidates):
                    x, y = candidates[idx]
                    for i in range(y + 1):
                        backtrack(cands + [x] * i, s + x * i, idx + 1)

        backtrack([], 0, 0)
        return self.ans

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        freq = sorted(Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans


if __name__ == '__main__':
    sol = Solution()
    candidates = [1, 1, 2, 3, 5, 6, 7]
    target = 8
    ret = sol.combinationSum2(candidates, target)
    print(ret)
