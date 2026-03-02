from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current = 0
        n = []
        for num in nums:
            current += num
            n.append(current)
        return n
       