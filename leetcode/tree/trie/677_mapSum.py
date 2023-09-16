# _*_ coding: utf-8 _*_
# @Time : 2022//26 11:11 PM 
# @Author : yefe
# @File : 677_mapSum

# class TrieNode:
#     def __init__(self):
#         self.val = 0
#         self.next = [None for _ in range(26)]
#
#
# class MapSum:
#     def __init__(self):
#         self.root = TrieNode()
#         self.map = {}
#
#     def insert(self, key: str, val: int) -> None:
#         delta = val
#         if key in self.map:
#             delta -= self.map[key]
#         self.map[key] = val
#         node = self.root
#         for c in key:
#             if node.next[ord(c) - ord('a')] is None:
#                 node.next[ord(c) - ord('a')] = TrieNode()
#             node = node.next[ord(c) - ord('a')]
#             node.val += delta
#
#     def sum(self, prefix: str) -> int:
#         node = self.root
#         for c in prefix:
#             if node.next[ord(c) - ord('a')] is None:
#                 return 0
#             node = node.next[ord(c) - ord('a')]
#         return node.val
class MapSum:

    def __init__(self):
        self.trie = dict()
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        if key in self.map:
            val = val-self.map[key]
            self.map[key] += val
        else:
            self.map[key] = val
        root = self.trie
        for k in key:
            if k not in root:
                root[k] = dict()
            root['val'] = root.get('val', 0)+val
            root = root[k]
        root['val'] = root.get('val', 0)+val

    def sum(self, prefix: str) -> int:
        root = self.trie
        for k in prefix:
            root = root.get(k, dict())
        return root.get('val', 0)


if __name__ == '__main__':
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    map_sum.insert("app", 2)
    map_sum.insert("apple", 5)
    map_sum.insert("apple", 1)
    ret = map_sum.sum("apple")
    print(ret)
