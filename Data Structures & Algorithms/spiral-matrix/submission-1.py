class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])

        # limits 
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        
        ans = []


        while right >= left and bottom >= top:
            # row
            for i in range(left, right+1):
                ans.append(matrix[top][i])

            # col
            for i in range(top+1, bottom+1):
                ans.append(matrix[i][right])

            # row
            for i in range(right-1, left-1, -1):
                if top!=bottom:
                    ans.append(matrix[bottom][i])

            # col
            for i in range(bottom-1, top, -1):
                if right!=left:
                    ans.append(matrix[i][left])

            top+=1
            bottom-=1
            left+=1
            right-=1

        return ans
        



    
        
        