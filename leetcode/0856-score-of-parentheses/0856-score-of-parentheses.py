class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for p in s:
            if p == "(":
                stack.append(0)
            else:
               val = stack.pop()
               stack[-1] += max(2*val , 1)
        return stack[0]

       






        