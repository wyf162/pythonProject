from collections import deque


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        s1 = 'aeiou'
        arr1 = [deque() for _ in range(5)]
        n = len(word)

        nums = [0] * n
        cnt = 0
        for i in range(n):
            nums[i] = cnt
            if word[i] in s1:
                cnt += 1
            else:
                cnt = 0

        i = 0
        cnt = 0
        ans = 0
        for j in range(n):
            if word[j] in s1:
                idx = s1.index(word[j])
                arr1[idx].append(j)
            else:
                cnt += 1
            while i < n and (cnt > k or (cnt == k and word[i] in s1 and len(arr1[s1.index(word[i])]) > 1)):
                if word[i] in s1:
                    idx = s1.index(word[i])
                    arr1[idx].popleft()
                else:
                    cnt -= 1
                i += 1
            if cnt == k and all(arr1):
                ans += nums[i] + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    word = 'iqeaouqi'
    k = 2
    ret = sol.countOfSubstrings(word, k)
    print(ret)
