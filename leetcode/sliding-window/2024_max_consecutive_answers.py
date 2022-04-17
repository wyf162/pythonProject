# _*_ coding: utf-8 _*_
# @Time : 2022/3/29 上午8:54 
# @Author : wangyefei
# @File : 2024_max_consecutive_answers.py

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))


if __name__ == '__main__':
    sol = Solution()
    answer_key = "TTFF"
    # answer_key = "TTFTTFTT"
    k = 2
    ret = sol.maxConsecutiveAnswers(answer_key, k)
    print(ret)
