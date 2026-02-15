from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3
        answer = [x - 1, x, x + 1]
        if sum(answer) == num:
            return answer
        else:
            return []
