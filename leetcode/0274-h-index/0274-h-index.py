class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = len(citations)
        citations.sort()
        for i in range(h):
            if citations[i] >= h-i:
                return h- i
        return 0


        

        