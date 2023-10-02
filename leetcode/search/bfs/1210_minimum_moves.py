# _*_ coding: utf-8 _*_
# @Time : 2023/01/14 2:15 PM 
# @Author : yefe
# @File : 1210_minimum_moves

from typing import List


class Direction:
    RIGHT = 'right'
    Down = 'down'


class Snake:
    def __init__(self, head: List[int], tail: List[int]):
        self.head = head
        self.tail = tail

    def to_right(self):
        self.head[1] += 1
        self.tail[1] += 1

    def to_down(self):
        self.head[0] += 1
        self.tail[0] += 1

    def clockwise(self):
        self.head[0] -= 1
        self.head[1] += 1

    def anticlockwise(self):
        self.head[0] += 1
        self.head[1] -= 1

    def revert_to_right(self):
        self.head[1] -= 1
        self.tail[1] -= 1

    def revert_to_down(self):
        self.head[0] -= 1
        self.tail[0] -= 1

    def revert_clockwise(self):
        self.head[0] += 1
        self.head[1] -= 1

    def revert_anticlockwise(self):
        self.head[0] -= 1
        self.head[1] += 1


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        ans = 100 * 100
        n = len(grid)

        def valid(min_x, min_y, max_x, max_y):
            tag = True
            if 0 <= min_x < n and 0 <= min_y < n and 0 <= max_x < n and 0 <= max_y < n:
                for x in range(min_x, max_x + 1):
                    for y in range(min_y, max_y + 1):
                        if grid[x][y] != 0:
                            tag = False
                            break
            else:
                tag = False
            return tag

        def dfs(snake: Snake, steps: int, pre=None):

            if snake.head == [n - 1, n - 1] and snake.tail == [n - 1, n - 2]:
                nonlocal ans
                ans = min(ans, steps)

            for func in ['to_right', 'to_down', 'clockwise', 'anticlockwise']:
                if pre in ['clockwise', 'anticlockwise'] and func in ['clockwise', 'anticlockwise']:
                    continue
                min_x, min_y = snake.tail
                max_x, max_y = snake.head
                getattr(snake, func)()
                steps += 1
                min_x = min(min_x, snake.tail[0])
                min_y = min(min_y, snake.tail[1])
                max_x = max(max_x, snake.head[0])
                max_y = max(max_y, snake.head[1])
                if valid(min_x, min_y, max_x, max_y):
                    dfs(snake, steps, func)
                getattr(snake, 'revert_' + func)()
                steps -= 1

        snake_obj = Snake([0, 1], [0, 0])
        dfs(snake_obj, 0)
        return ans


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0]]
    # grid = [[0, 0],
    #         [0, 0]]
    ret = sol.minimumMoves(grid)
    print(ret)
