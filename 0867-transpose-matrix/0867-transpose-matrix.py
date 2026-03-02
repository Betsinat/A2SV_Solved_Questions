class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        T =[]
        for j in range(col):
            n_row = []
            for i in range(row):
                n_row.append(matrix[i][j])
            T.append(n_row)
        return T







        