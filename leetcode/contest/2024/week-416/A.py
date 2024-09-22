
from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        st = set(bannedWords)
        ans = 0
        for msg in message:
            if msg in st:
                ans += 1
        return ans >= 2
