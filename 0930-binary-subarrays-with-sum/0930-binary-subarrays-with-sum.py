class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0:1}
        total = 0
        count = 0
        for n in nums:
            total += n
            if total - goal in freq:
                count += freq[total - goal]
            freq[total] = freq.get(total, 0) + 1
        return count
        
        