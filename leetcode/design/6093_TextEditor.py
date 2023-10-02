# _*_ coding: utf-8 _*_
# @Time : 2022/06/05 10:46 AM 
# @Author : yefe
# @File : 6093_TextEditor


class TextEditor2:

    def __init__(self):
        self.text = [''] * 80000
        self.cursor = 0
        self.length = 0

    def addText(self, text: str) -> None:
        if self.cursor < self.length:
            for i in range(self.length, self.cursor - 1, -1):
                print(i, i + len(text) - self.cursor)
                self.text[i + len(text) - self.cursor] = self.text[i]

        for i in range(len(text)):
            self.text[self.cursor] = text[i]
            self.cursor += 1
            self.length += 1

    def deleteText(self, k: int) -> int:
        if self.cursor <= k:
            for i in range(self.cursor, self.length + 1):
                self.text[i - self.cursor] = self.text[i]
                self.text[i] = ''
            self.length = self.length - self.cursor
            k = self.cursor
            self.cursor = 0
            return k
        else:
            for i in range(self.cursor, self.length + 1):
                self.text[i - k] = self.text[i]
                self.text[i] = ''
            self.length = self.length - k
            self.cursor -= k
            return k

    def cursorLeft(self, k: int) -> str:
        if self.cursor <= k:
            self.cursor = 0
            return "".join(self.text[max(self.cursor - 10, 0):self.cursor])
        else:
            self.cursor -= k
            return "".join(self.text[max(self.cursor - 10, 0):self.cursor])

    def cursorRight(self, k: int) -> str:
        if self.cursor + k >= self.length:
            self.cursor = self.length
            return "".join(self.text[max(self.cursor - 10, 0):self.cursor])
        else:
            self.cursor += k
            return "".join(self.text[max(self.cursor - 10, 0):self.cursor])


class TextEditor3:

    def __init__(self):
        self.text = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        if k < self.cursor:
            self.text = self.text[:self.cursor - k] + self.text[self.cursor:]
            self.cursor -= k
            return k
        else:
            self.text = self.text[self.cursor:]
            k = self.cursor
            self.cursor = 0
            return k

    def cursorLeft(self, k: int) -> str:
        if self.cursor>k:
            self.cursor = self.cursor-k
            ret = self.text[max(self.cursor - 10, 0):self.cursor]
        else:
            self.cursor = 0
            ret = self.text[max(self.cursor - 10, 0):self.cursor]
        return ret

    def cursorRight(self, k: int) -> str:
        if self.cursor+k <len(self.text):
            self.cursor = self.cursor + k
            ret = self.text[max(self.cursor - 10, 0):self.cursor]
        else:
            self.cursor = len(self.text)
            ret = self.text[max(self.cursor - 10, 0):self.cursor]
        return ret


class Node:

    def __init__(self, ch=''):
        self.prev = None
        self.next = None
        self.ch = ch

    # 在self后面插入node, 并返回该node
    def insert(self, node: 'Node') -> 'Node':
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    # 从链表中删除self
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class TextEditor:
    def __init__(self):
        self.root = self.cur = Node()  # 哨兵节点
        self.root.prev = self.root
        self.root.next = self.root  # 初始化双向链表，下面判断节点的 next 若为 self.root，则表示 next 为空

    def addText(self, text: str) -> None:
        for ch in text:
            self.cur = self.cur.insert(Node(ch))

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            self.cur.next.remove()
            k -= 1
        return k0 - k

    def text(self) -> str:
        s = []
        k, cur = 10, self.cur
        while k and cur != self.root:
            s.append(cur.ch)
            cur = cur.prev
            k -= 1
        return ''.join(reversed(s))

    def cursorLeft(self, k: int) -> str:
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.cur.next != self.root:
            self.cur = self.cur.next
            k -= 1
        return self.text()


if __name__ == '__main__':
    # cmds = ["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft",
    #         "cursorRight"]
    # parms = [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]

    # cmds = ["TextEditor", "addText", "cursorLeft", "deleteText", "cursorLeft", "addText", "cursorRight"]
    # parms = [[], ["bxyackuncqzcqo"], [12], [3], [5], ["osdhyvqxf"], [10]]

    cmds = ["TextEditor", "addText", "addText", "cursorLeft", "addText", "cursorLeft", "addText", "addText"]
    parms = [[], ["ydqikzumibbigl"], ["nuvska"], [3], ["sgtiuhxsnddefr"], [18], ["mdpmxkbliikqviikbt"],
             ["lfveldxwzbotb"]]

    text_editor = TextEditor()
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(text_editor, cmd)(*parm)
        print(ret)
