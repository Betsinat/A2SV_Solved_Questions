class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       arr = [i for i in range(len(nums) + 1)]
       for i in range(len(arr)):
          if arr[i] not in nums:
            return arr[i]
        
        
