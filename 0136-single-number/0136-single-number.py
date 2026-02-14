class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count =  Counter(nums)
        for key in count:
            if count[key] == 1:
                return key