class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left =  1
        right =  max(candies)
        while left <= right:
            mid = (left + right )// 2
            tot =  sum(c // mid for c in candies)
            if tot >= k:
                left = mid + 1
            else:
                right =  mid - 1
        return right


            
        