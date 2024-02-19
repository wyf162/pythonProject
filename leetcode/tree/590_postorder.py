from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stk = [[root, 0]]
        ans = []
        while stk:
            cur, state = stk.pop()
            if state == 0:
                stk.append([cur, 1])
                for child in cur.children[::-1]:
                    stk.append([child, 0])
            else:
                ans.append(cur.val)
        return ans
