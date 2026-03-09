class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        c = 0
        for log in logs:
            if log == "../":
                c -= 1 if c > 0 else 0
            else:
                if log == "./":
                    c+= 0
                else:
                    c += 1
        return c