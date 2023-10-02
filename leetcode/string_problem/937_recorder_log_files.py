# _*_ coding: utf-8 _*_
# @Time : 2022/05/03 2:59 AM 
# @Author : yefe
# @File : 937_recorder_log_files
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_log = []
        number_log = []
        for log in logs:
            tag = log.split(' ')[0]
            if log.split(' ')[1].isdigit():
                number_log.append(log)
            else:
                content = " ".join(log.split(' ')[1:])
                alpha_log.append((content, tag))
        alpha_log.sort(key=lambda x: (x[0], x[1]))
        alpha_log = [y+' '+x for x, y in alpha_log]
        return alpha_log+number_log


if __name__ == '__main__':
    sol = Solution()
    # logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    logs = ["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]
    ret = sol.reorderLogFiles(logs)
    print(ret)
