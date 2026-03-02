from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = [0] * len(nums)  
        n[0] = nums[0]      
        for i in range(1, len(nums)):
            n[i] = nums[i] + n[i - 1]
        return n  
