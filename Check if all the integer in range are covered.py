class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            covered = False
            for start , end in ranges:
                if start <= x <= end:
                    covered = True
                    break
            if not covered:
                return False
        return True
        



        
