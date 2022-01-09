# -*- coding : utf-8 -*-
# @Time: 2021/12/25 22:24
# @Author: yefei.wang
# @File: 20211225.py
from copy import deepcopy
from typing import List
from collections import defaultdict


class Solution2:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]):
        n = len(recipes)
        # topo sort
        dag = defaultdict(list)
        recipes_set = set(recipes)
        recipes_hst = {recipe: i for i, recipe in enumerate(recipes)}
        for i in range(n):
            for ingredient in ingredients[i]:
                j = recipes_hst.get(ingredient)
                if j is not None:
                    dag[j].append(i)

        in_degree = [0] * n
        for i in range(n):
            for j in dag.get(i, list()):
                in_degree[j] += 1
        topo_sort_list = []
        dq = []
        for i in range(n):
            if in_degree[i] == 0:
                dq.append(i)
        while dq:
            node = dq.pop(0)
            topo_sort_list.append(node)
            for j in dag.get(node, list()):
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    dq.append(j)
        # print('topo sort list', topo_sort_list)

        supplies_hst = {supply: True for supply in supplies}
        ans = []
        for i in topo_sort_list:
            tag = True
            for ingredient in ingredients[i]:
                if supplies_hst.get(ingredient):
                    continue
                else:
                    tag = False
                    break
            if tag:
                ans.append(recipes[i])
                supplies_hst[recipes[i]] = True
        return ans





class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stk = list()
        n = len(s)
        for i in range(n):
            if not stk:
                if locked[i]=='0':
                    stk.append('*')
                else:
                    stk.append(s[i])
            else:
                if locked[i]=='0':
                    if stk[-1]=='(':
                        stk.pop()
                    else:
                        stk.append('*')
                else:
                    if s[i]==')' and stk[-1]=='(':
                        stk.pop()
                    else:
                        stk.append(s[i])

        print(stk)


if __name__ == "__main__":
    sol = Solution()
    s = "))()))"
    locked = "010100"
    ans = sol.canBeValid(s,locked)

    # recipes = ["sandwich", "bread"]
    # ingredients = [["bread", "meat"], ["yeast", "flour"],]
    # supplies = ["yeast", "flour", "meat"]
    # recipes = ["bread", "sandwich"]
    # ingredients = [["yeast", "flour"], ["bread", "meat"]]
    # supplies = ["yeast", "flour", "meat"]
    # recipes = ["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"]
    # ingredients =[["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
    #  ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"],
    #  ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]]
    # supplies= ["f", "hveml", "cpivl", "d"]
    # ans = sol.findAllRecipes(recipes, ingredients, supplies)
    # print(ans)
