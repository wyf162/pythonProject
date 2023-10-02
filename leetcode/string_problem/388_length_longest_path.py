# _*_ coding: utf-8 _*_
# @Time : 2022/4/20 上午8:40 
# @Author : wangyefei
# @File : 388_length_longest_path.py

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input += "\n"
        stk = list()
        cur_len = 0
        ans = 0
        i, n = 0, len(input)
        j = input[i:].find("\n")
        while 0 < j < len(input):
            h = len(stk)
            indents = 0
            while input[i:i + 1] == "\t":
                indents += 1
                i += 1
            fp = input[i:j]

            while len(stk) > indents:
                cur_len -= len(stk.pop())
            stk.append(fp)
            cur_len += len(fp)
            if '.' in fp:
                ans = max(ans, cur_len + len(stk) - 1)
            print(stk)
            i = j + 1
            t = input[i:].find("\n")
            print(t)
            if t > 0:
                j = i + t
            else:
                break
        return ans

    def lengthLongestPaht(self, input: str) -> int:
        res = 0
        depth_length_map = {-1: 0}
        for line in input.split('\n'):
            depth = line.count('\t')
            depth_length_map[depth] = depth_length_map[depth-1]+len(line)-depth
            if line.count('.'):
                res = max(res, depth_length_map[depth]+depth)
        return res


if __name__ == '__main__':
    sol = Solution()
    # input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    # input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    input = "file1.txt\nfile2.txt\nlongfile.txt"
    ret = sol.lengthLongestPath(input)
    print(ret)
