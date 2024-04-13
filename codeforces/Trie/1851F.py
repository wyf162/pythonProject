# -*- coding : utf-8 -*-
# @Time: 2023/9/13 20:03
# @Author: yefei.wang
# @File: 1851f.py


class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.idx = -1


class Trie:

    def __init__(self, h):
        self.h = h
        self.root = TrieNode()

    def insert(self, num, idx):
        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr] is None:
                node.children[lr] = TrieNode()
            node = node.children[lr]
        node.idx = idx

    def minimum_xor(self, num):
        mx = 0
        mask = 0

        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr]:
                node = node.children[lr]
                if lr == 0:
                    mask |= (1 << i)
                mx |= (1 << i)
            elif node.children[lr ^ 1]:
                node = node.children[lr ^ 1]
            else:
                print('break')
                break
        return mx, mask, node.idx


def solve(n, k, nums):
    trie = Trie(k)
    trie.insert(nums[0], 0)
    ans = 0
    l, r, x = 0, 1, 0
    for j, num in enumerate(nums[1:]):
        mx, mask, i = trie.minimum_xor(num)
        if mx > ans:
            ans = mx
            l, r, x = i, j + 1, mask
        trie.insert(num, j + 1)
    print(l + 1, r + 1, x)
    # print(f"max: {(nums[l] ^ x) & (nums[r] ^ x)}")


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        solve(n, k, nums)


if __name__ == '__main__':
    # sys.stdin = open('input.txt', 'r')
    main()
