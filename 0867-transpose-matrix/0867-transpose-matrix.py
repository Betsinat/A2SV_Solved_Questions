class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [list(row) for row in zip(*matrix)]
        return transpose








        