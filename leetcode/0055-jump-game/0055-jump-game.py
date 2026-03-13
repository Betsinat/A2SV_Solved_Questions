class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        _max = 0 
        for i in range(len(nums)):
            if i > _max:
                return False
            else:
                _max= max(_max , i + nums[i])
        return True
      