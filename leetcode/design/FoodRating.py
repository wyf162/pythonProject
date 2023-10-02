# -*- coding : utf-8 -*-
# @Time: 2022/7/24 10:54
# @Author: yefei.wang
# @File: FoodRating.py
from typing import List
from sortedcontainers import SortedSet
from collections import defaultdict


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food2rate = dict()
        self.food2cuisine = dict()
        self.cuisine2rate = defaultdict(SortedSet, **{"key": lambda x: (x[0], x[1])})
        n = len(foods)
        for i in range(n):
            self.food2rate[foods[i]] = ratings[i]
            self.food2cuisine[foods[i]] = cuisines[i]
            self.cuisine2rate[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        pre_rate = self.food2rate[food]
        cuisine = self.food2cuisine[food]
        self.cuisine2rate[cuisine].remove((-pre_rate, food))

        self.food2rate[food] = newRating
        self.cuisine2rate[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine2rate[cuisine][0][1]


if __name__ == '__main__':
    cmds = ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating",
            "highestRated"]
    parms = [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
              ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"],
             ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

    food_ratings = FoodRatings(*parms[0])
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(food_ratings, cmd)(*parm)
        print(ret)