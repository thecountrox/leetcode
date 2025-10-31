"""
In this problem we have to do the following:
- Obtain Substrings
- Check if they are palindrome
- keep track of them so that we can run through all of them recursively
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def backtrack(current: List[str], idx: int) -> None:
            # base case: we have run out of things to add
            if idx == n:
                res.append(current.copy())
                return

            # recursion
            for i in range(idx, n):
                substr = s[idx : i + 1]
                if is_palindrome(substr):
                    current.append(substr)
                    backtrack(current, i + 1)
                    current.pop()

        backtrack([], 0)
        return res


s = Solution()
print(s.partition("aab"))

