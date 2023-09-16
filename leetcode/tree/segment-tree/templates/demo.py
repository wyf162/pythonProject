# _*_ coding: utf-8 _*_
# @Time : 2022/10/22 4:59 PM 
# @Author : yefe
# @File : demo

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0


class SegmentTree:

    def __init__(self):
        self.root = Node()
        self.n = 10 ** 9

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val = val
            return
        self.push_down(node)
        mid = (start + end) >> 1
        if l <= mid:
            self.update(node.left, start, mid, l, r, val)
        if r > mid:
            self.update(node.right, mid + 1, end, l, r, val)
        self.push_up(node)

    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return node.val
        self.push_down(node)
        mid = (start + end) >> 1
        ans = 0
        if l <= mid:
            ans = self.query(node.left, start, mid, l, r)
        if r > mid:
            ans = max(ans, self.query(node.right, mid + 1, end, l, r))
        return ans

    @staticmethod
    def push_down(node):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()


    @staticmethod
    def push_up(node):
        node.val = max(node.left.val, node.right.val)


if __name__ == '__main__':
    segment_tree = SegmentTree()
    segment_tree.update(segment_tree.root, 0, segment_tree.n, 1, 1, 10)
    segment_tree.update(segment_tree.root, 0, segment_tree.n, 10, 10, 100)

    ret = segment_tree.query(segment_tree.root, 0, segment_tree.n, 1, 1)
    print(ret)
    ret = segment_tree.query(segment_tree.root, 0, segment_tree.n, 2, 2)
    print(ret)
    ret = segment_tree.query(segment_tree.root, 0, segment_tree.n, 1, 10)
    print(ret)


