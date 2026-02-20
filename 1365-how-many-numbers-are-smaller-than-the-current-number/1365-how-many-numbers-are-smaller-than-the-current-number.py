class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            arr.append(count)
        return arr


        
       

    
       

     


      