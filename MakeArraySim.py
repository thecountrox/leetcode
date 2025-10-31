from typing import List

class Solution:
    def countValidSelections(nums: List[int]) -> int:

        def getValidStartingPos()-> list[int]:
            out = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    out.append((i,'l'))
                    out.append((i,'r'))
            return out

        def validate(out: list[int])-> None:
            res = 0
            for (start,dirr) in out:
                res+= simulate(start, dirr, nums)
            return res

        def simulate(start: int, dirr: chr, nums: list[int])-> None:
            # while i is kept inside the bounds
            i = start
            while i > 0 and i < len(nums):
                if nums[i] > 0:
                    nums[i] -= 1
                    if dirr == 'l':
                        dirr = 'r'
                    else:
                        dirr = 'l'

                if dirr == 'l':
                    i-= 1
                else:
                    i+=1

            if all(x == 0 for x in nums):
                return 1
            else:
                return 0
        out = getValidStartingPos()
        return(validate(out))



a = Solution()
print(Solution.countValidSelections([1,0,2,0,3]))
