
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        rsum = 0
        for i in range(len(nums)):
            rsum += nums[i]
            res.append(rsum)
        return res