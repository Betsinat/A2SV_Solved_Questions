class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        majority = []
        for num , key in count.items():
            if key > len(nums)//3:
               majority.append(num)
        return majority
