class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate(m):
            for i in range(n):
                for j in range(i+1 , n):
                    m[i][j] ,  m[j][i] = m[j][i] , m[i][j]
            for row in m:
                row.reverse()
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        return False
        

            

       

        