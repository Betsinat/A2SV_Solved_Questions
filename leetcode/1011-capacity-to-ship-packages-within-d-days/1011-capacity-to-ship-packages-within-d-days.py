class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
       
        while  left < right:
            mid = (left + right) // 2
            day = 1
            curr = 0
            for w in weights:
                if curr + w > mid:
                    day += 1
                    curr = 0
                curr += w
            if day <= days:
                right = mid
            else:
                left = mid + 1
        return left

         

            

            
            
        