class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1} 
        total = 0
        count = 0
        
        for n in nums:
            total += n
            remainder = total % k
            remainder = (remainder + k) % k
            if remainder in freq:
                count += freq[remainder]
            freq[remainder] = freq.get(remainder, 0) + 1
        
        return count

            
        




        