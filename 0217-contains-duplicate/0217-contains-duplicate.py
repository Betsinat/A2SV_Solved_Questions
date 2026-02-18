class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        for value in count.values():
            if value > 1:
                return True
        return False


        