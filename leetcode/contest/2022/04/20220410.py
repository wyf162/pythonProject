# _*_ coding: utf-8 _*_
# @Time : 2022/4/10 下午4:59 
# @Author : wangyefei
# @File : 20220410.py
from typing import List
from collections import defaultdict


class Solution:
    def deleteText(self, article: str, index: int) -> str:
        s = index
        while s > 0 and article[s] != " ":
            s -= 1

        t = index
        while t < len(article) and article[t] != " ":
            t += 1

        return article[:s] + article[t:] if article[:s] else article[t+1:]

    def numFlowers(self, roads: List[List[int]]) -> int:
        adj_tbl = defaultdict(list)
        for road in roads:
            s, t = road
            adj_tbl[s].append(t)
            adj_tbl[t].append(s)

        ret = 0
        for k,v in adj_tbl.items():
            ret = max(ret, len(v)+1)
        return ret

    def lightSticks(self, height: int, width: int, indices: List[int]) -> List[int]:
        pass




    def goShopping(self, priceA: List[int], priceB: List[int]) -> int:
        pass




if __name__ == '__main__':
    sol = Solution()
    article = "Singing"
    index = 6
    ret = sol.deleteText(article, index)
    print(ret)
