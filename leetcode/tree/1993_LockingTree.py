# _*_ coding: utf-8 _*_
# @Time : 2022/11/14 10:28 PM 
# @Author : yefe
# @File : 1993_LockingTree

from typing import List
from collections import defaultdict


class LockingTree:

    def __init__(self, parent: List[int]):
        self.n = len(parent)
        self.children = defaultdict(list)
        self.parent = dict()

        for son, father in enumerate(parent):
            self.parent[son] = father
            self.children[father].append(son)

        self.locker = dict()

    def lock(self, num: int, user: int) -> bool:
        if self.locker.get(num) is None:
            self.locker[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locker.get(num) == user:
            self.locker[num] = None
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locker.get(num) is None and self.get_ancestors(num) and self.get_descendants(num):
            self.lock(num, user)
            self.unlock_descendants(num)
            return True
        else:
            return False

    def get_ancestors(self, num: int) -> bool:
        if self.parent.get(num) is None:
            return True
        else:
            par = self.parent[num]
            if self.locker.get(par) is not None:
                return False
            else:
                return self.get_ancestors(par)

    def get_descendants(self, num: int) -> bool:

        ret = False
        for child in self.children[num]:
            if self.locker.get(child) is not None:
                ret = ret | True
            else:
                ret = ret | self.get_descendants(child)
        return ret

    def unlock_descendants(self, num: int) -> None:
        for child in self.children[num]:
            if self.locker.get(child) is not None:
                self.locker[child] = None
            self.unlock_descendants(child)


if __name__ == '__main__':
    cmds = ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
    parms = [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]

    locking_tree = LockingTree(parms[0][0])
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(locking_tree, cmd)(*parm)
        print(ret)
