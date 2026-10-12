class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # if we reach 0, iterate through m and n, and mark row / col as *
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 or matrix[i][j] == "*":
                    continue

                for a in range(n):
                    if matrix[i][a] != 0:
                        matrix[i][a] = "*" 

                for b in range(m):
                    if matrix[b][j] != 0:
                        matrix[b][j] = "*"
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0



        


        