class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for p in s:
            if p == "(":
                stack.append(0)
            else:
                val = stack.pop()
                score = 1 if val == 0 else 2 * val
                
                if stack:
                    stack[-1] += score
                else:
                    res += score
        
        return res

       






        