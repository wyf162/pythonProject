# _*_ coding: utf-8 _*_
# @Time : 2022/05/23 9:23 PM 
# @Author : yefe
# @File : 675_cut_off_tree
import copy
from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])
        all_step = 0
        trees.sort()
        start = [0, 0]
        for tree in trees:
            end = tree[1:]
            step = self.bfs(start, end, forest)
            if step >= 0:
                all_step += step
                forest[end[0]][end[1]] = 1
                start = copy.deepcopy(end)
            else:
                return -1
        return all_step

    def bfs(self, start, end, graph):
        if start == end:
            return 0
        m = len(graph)
        n = len(graph[0])
        unvisited = [[True for j in range(n)] for i in range(m)]
        step = 0
        q = deque()
        q.append(start)
        unvisited[start[0]][start[1]] = False
        while q:
            step += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if nx == end[0] and ny == end[1]:
                            return step
                        elif graph[nx][ny] >= 1 and unvisited[nx][ny]:
                            q.append([nx, ny])
                            unvisited[nx][ny] = False
        return -1


if __name__ == '__main__':
    # forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
    # forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]
    # forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]
    # forest = [[0, 0, 0, 3528, 2256, 9394, 3153],
    #           [8740, 1758, 6319, 3400, 4502, 7475, 6812],
    #           [0, 0, 3079, 6312, 0, 0, 0],
    #           [6828, 0, 0, 0, 0, 0, 8145],
    #           [6964, 4631, 0, 0, 0, 4811, 0],
    #           [0, 0, 0, 0, 9734, 4696, 4246],
    #           [3413, 8887, 0, 4766, 0, 0, 0],
    #           [7739, 0, 0, 2920, 0, 5321, 2250],
    #           [3032, 0, 3015, 0, 3269, 8582, 0]]
    forest = [[54581641,64080174,24346381,69107959],
              [86374198,61363882,68783324,79706116],
              [668150,92178815,89819108,94701471],
              [83920491,22724204,46281641,47531096],
              [89078499,18904913,25462145,60813308]]
    ret = Solution().cutOffTree(forest)
    print(ret)
