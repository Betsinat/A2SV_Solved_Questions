class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            digits = [int(d) for d in str(n)]
            s = 0
            for i in range(len(digits)):
               s += digits[i] * digits[i]
            if s == 1:
               return True
            n = s
        return False
    
        
        
        