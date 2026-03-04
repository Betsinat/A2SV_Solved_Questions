class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        total = 0
        count = 0
        for n in nums:
            total += n
            if total - k in freq:
                count += freq[total - k]
            freq[total] = freq.get(total, 0) + 1
        return count

        