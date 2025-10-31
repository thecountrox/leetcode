"""
you are given an array of numbers and a target , return a list of all unique combinations of numbers where chosen numbers add to the target.
any order is good.

same number can be chosen unlimited times but the sequence of numbers should be unique. so order does not really matter.

each iternation or lookup on our backtrack should:
take or pass, until it sums upto or more than 7.
if it is more than 7 then we dont gaf and dont add it.
if it sums to 7 then add it and return.
we continue until we exhaust the entire thing.
Good luck recursion limit. o7.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(target: int, idx: int, current_combination):
            # Base Case check exact match
            if target == 0:
                res.append(list(current_combination))

            # Base Case Prune
            if target < 0:
                return

            # recursion step
            for i in range(idx, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(target - candidates[i], i, current_combination)
                current_combination.pop()

        backtrack(target, 0, [])
        return res


s = Solution()
print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
