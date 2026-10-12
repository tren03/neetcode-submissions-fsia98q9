class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # if we reach 0, iterate through m and n, and mark row / col as *
        m = len(matrix)
        n = len(matrix[0])
        
        row = [False] * m
        col = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 0:
                    col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
            

        
      


        


        