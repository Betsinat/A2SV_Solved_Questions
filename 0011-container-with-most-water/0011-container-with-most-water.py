class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left , right = 0 , len(height) - 1
        current = 0
        while left < right:
            maxw = min(height[left] , height[right]) * (right - left)
            if maxw > current:
                current = maxw
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return current

            

            


        