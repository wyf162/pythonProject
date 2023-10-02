# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 10:28 AM 
# @Author : yefe
# @File : week-307-20220821

from typing import List, Optional
from collections import Counter, deque, defaultdict
from string import digits
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


class Solution:
    def minNumberOfHours(self,
                         initialEnergy: int,
                         initialExperience: int,
                         energy: List[int],
                         experience: List[int]) -> int:
        ret = 0
        ix, iy = initialEnergy, initialExperience
        for x, y in zip(energy, experience):
            if ix > x and iy > y:
                ix -= x
                iy += y
            elif ix > x and iy <= y:
                ret += y + 1 - iy
                ix -= x
                iy += y + y + 1 - iy
            elif ix <= x and iy > y:
                ret += x + 1 - ix
                ix = 1
                iy += y
            elif ix <= x and iy <= y:
                ret += y + 1 - iy
                ret += x + 1 - ix
                ix = 1
                iy += y + y + 1 - iy
        return ret

    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)
        ret = ""

        is_start_with_zero = False
        is_with_odd = ""
        for digit in '987654321':
            if cnt[digit] > 1:
                is_start_with_zero = True
                # print(digit * (cnt[digit] // 2))
                ret = ret + digit * (cnt[digit] // 2)
            if cnt[digit] % 2 == 1 and is_with_odd == '':
                is_with_odd = digit

        if is_start_with_zero:
            ret = ret + '0' * (cnt['0'] // 2)

        if is_with_odd:
            ret = ret + is_with_odd + ret[::-1]
        elif ret and cnt['0'] % 2 == 1:
            ret = ret + '0' + ret[::-1]
        elif ret:
            ret = ret + ret[::-1]
        elif ret == "" and cnt['0']:
            ret = "0"

        return ret

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        hst = defaultdict(list)

        def dfs(node):
            if not node:
                return
            if node.left:
                hst[node.val].append(node.left.val)
                hst[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                hst[node.val].append(node.right.val)
                hst[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)

        visited = set()

        q = deque()
        q.append(start)
        visited.add(start)

        ts = 0
        while q and len(visited) < len(hst):
            ts += 1
            for _ in range(len(q)):
                x = q.popleft()
                for y in hst[x]:
                    if y not in visited:
                        q.append(y)
                        visited.add(y)
        return ts

    def kSum(self, nums: List[int], k: int) -> int:
        su = 0
        for i, x in enumerate(nums):
            if x >= 0:
                su += x
            else:
                nums[i] = -x

        nums.sort()
        h = [(-su, 0)]
        while k > 1:
            k -= 1
            s, i = heapq.heappop(h)
            if i < len(nums):
                heapq.heappush(h, (s + nums[i], i + 1))
                if i:
                    heapq.heappush(h, (s + nums[i] - nums[i - 1], i + 1))
        return -h[0][0]


if __name__ == '__main__':
    sol = Solution()
    inputs = "[1, 5, 3, null, 4, 10, 6, 9, 2]"
    start = 3
    root = stringToTreeNode(inputs)
    ret = sol.amountOfTime(root, start)
    print(ret)

    # num = "220"
    # num = "444947137"
    # num = "000099"
    # num = "00001105"
    # # num = "00000"
    # ret = sol.largestPalindromic(num)
    # print(ret)

    # initialEnergy = 5
    # initialExperience = 3
    # energy = [1, 4, 3, 2]
    # experience = [2, 6, 3, 1]
    # initialEnergy = 1
    # initialExperience = 1
    # energy = [1, 1, 1, 1]
    # experience = [1, 1, 1, 50]
    # ret = sol.minNumberOfHours(initialEnergy, initialExperience, energy, experience)
    # print(ret)
