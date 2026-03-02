class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # traverse top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # traverse right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # traverse bottom row (check top <= bottom)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # traverse left column (check left <= right)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

        
