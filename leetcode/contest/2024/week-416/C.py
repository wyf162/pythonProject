

def compare(nums1, nums2):
    for i in range(26):
        if nums1[i] < nums2[i]:
            return False
    return True


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:

        cnt2 = [0] * 26
        for c in word2:
            idx = ord(c) - ord('a')
            cnt2[idx] += 1

        ans = 0
        i1 = 0
        n = len(word1)
        cnt1 = [0] * 26
        for i2, c in enumerate(word1):
            idx = ord(c) - ord('a')
            cnt1[idx] += 1

            while i1 < n and compare(cnt1, cnt2):
                idx = ord(word1[i1]) - ord('a')
                cnt1[idx] -= 1
                i1 += 1
                ans += n - i2
        return ans


if __name__ == "__main__":
    sol = Solution()
    word1 = "dcbdcdccb"
    word2 = "cdd"
    ret = sol.validSubstringCount(word1, word2)
    print(ret)
