# _*_ coding: utf-8 _*_
# @Time : 2022/12/31 7:31 PM 
# @Author : yefe
# @File : 855_ExamRoom


class ListNode:

    def __init__(self, val, nex=None):
        self.val = val
        self.nex = nex


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.root = None

    def seat(self) -> int:
        if self.root is None:
            self.root = ListNode(0)
            return 0
        first_gap = self.root.val - 0
        node = self.root
        max_gap, pre_node, new_node_val = 0, None, -1
        while node.nex:
            gap = (node.nex.val - node.val) // 2
            if gap > max_gap:
                max_gap, pre_node, new_node_val = gap, node, node.val + gap
            node = node.nex

        last_gap = self.n - 1 - node.val
        if last_gap > max_gap and last_gap > first_gap:
            node.nex = ListNode(self.n - 1, None)
            return self.n - 1
        if max_gap >= last_gap and max_gap > first_gap:
            pre_node.nex = ListNode(new_node_val, pre_node.nex)
            return new_node_val
        self.root = ListNode(0, self.root)
        return 0

    def leave(self, p: int) -> None:
        if self.root and self.root.val == p:
            self.root = self.root.nex
        node = self.root
        while node:
            if node.nex and node.nex.val == p:
                node.nex = node.nex.nex
                return
            node = node.nex


if __name__ == '__main__':
    cmds = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
    parms = [[10], [], [], [], [], [4], []]

    exam_room = ExamRoom(parms[0][0])
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(exam_room, cmd)(*parm)
        print(ret)
