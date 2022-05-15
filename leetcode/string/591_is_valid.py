# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 11:24 AM 
# @Author : yefe
# @File : 591_is_valid

class Solution:
    def isValid(self, code: str) -> bool:
        tags = []
        i, n = 0, len(code)
        while i < n:
            if code[i] != '<':
                if not tags:
                    return False
                i += 1
                continue
            if i == n - 1:
                return False
            if code[i + 1] == "/":
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 2:j]
                if not tags or tags[-1] != tagname:
                    return False
                tags.pop()
                i = j + 1
                if not tags and i != n:
                    return False
            elif code[i + 1] == "!":
                if not tags:
                    return False
                cdata = code[i + 2:i + 9]
                if cdata != "[CDATA[":
                    return False
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 1
            else:
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 1:j]
                if not 1 <= len(tagname) <= 9 or not all(ch.isupper() for ch in tagname):
                    return False
                tags.append(tagname)
                i = j + 1
        return not tags


if __name__ == '__main__':
    sol = Solution()
    code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
    ret = sol.isValid(code)
    print(ret)
