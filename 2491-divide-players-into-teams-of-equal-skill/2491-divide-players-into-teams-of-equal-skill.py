class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        sk = sorted(skill)
        left , right = 0 , len(sk) - 1
        sum = sk[left] + sk[right]
        total = 0
        while left < right:
            if sk[left] + sk[right] != sum:
                return -1
            total += sk[left] * sk[right]
            left += 1
            right -= 1
        return total
        