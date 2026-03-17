class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        smallest =  float('-inf')
        for num in reversed(nums):
            if num < smallest:
                return True
            while stack and num > stack[-1]:
                smallest =  stack.pop()
            stack.append(num)
        return False
       




        
            


        
            


        