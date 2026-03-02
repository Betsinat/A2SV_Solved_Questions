class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols =  len(matrix[0])
        zeroc = [False]*cols
        zeror = [False]*rows
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] ==  0:
                    zeroc[j] =True
                    zeror[i] =True
        for i in range(rows):
             for j in range(cols):
                if zeroc[j] == True or zeror[i] ==True:
                    matrix[i][j] = 0
        return matrix
                    
                
    

