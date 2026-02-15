class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer +=  [int(d) for d in str(num)]
        return answer
      

        