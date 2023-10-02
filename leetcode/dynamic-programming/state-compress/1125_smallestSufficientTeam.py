# -*- coding : utf-8 -*-
# @Time: 2023/9/19 21:03
# @Author: yefei.wang
# @File: 1125_smallestSufficientTeam.py
from typing import List


def get_array(n):
    nums = [i for i in range(1, (1 << n))]
    nums.sort(key=lambda x: bin(x).count('1'))
    return nums


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = [None] * (1 << n)
        dp[0] = []
        for i, p in enumerate(people):
            cur_skill = 0
            for s in p:
                cur_skill |= 1 << skill_index[s]
            for prev in range(1 << n):
                if dp[prev] is None:
                    continue
                comb = prev | cur_skill
                if dp[comb] is None or len(dp[comb]) > len(dp[prev]) + 1:
                    dp[comb] = dp[prev] + [i]
        return dp[(1 << n) - 1]


if __name__ == '__main__':
    sol = Solution()
    req_skills = ["mwobudvo", "goczubcwnfze", "yspbsez", "pf", "ey", "hkq"]
    people = [[], ["mwobudvo"], ["hkq"], ["pf"], ["pf"], ["mwobudvo", "pf"], [], ["yspbsez"], [], ["hkq"], [], [],
              ["goczubcwnfze", "pf", "hkq"], ["goczubcwnfze"], ["hkq"], ["mwobudvo"], [], ["mwobudvo", "pf"],
              ["pf", "ey"], ["mwobudvo"], ["hkq"], [], ["pf"], ["mwobudvo", "yspbsez"], ["mwobudvo", "goczubcwnfze"],
              ["goczubcwnfze", "pf"], ["goczubcwnfze"], ["goczubcwnfze"], ["mwobudvo"], ["mwobudvo", "goczubcwnfze"],
              [], ["goczubcwnfze"], [], ["goczubcwnfze"], ["mwobudvo"], [], ["hkq"], ["yspbsez"], ["mwobudvo"],
              ["goczubcwnfze", "ey"]]
    ret = sol.smallestSufficientTeam(req_skills, people)
    print(ret)
    print(req_skills)
    for idx in ret:
        print(people[idx])
