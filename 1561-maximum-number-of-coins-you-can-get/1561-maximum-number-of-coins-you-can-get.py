class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a = int(len(piles) / 3)
        sum = 0
        for i in range(a , len(piles) , 2):
           sum += piles[i]
        return sum

        