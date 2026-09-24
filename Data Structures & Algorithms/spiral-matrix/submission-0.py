class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        ans = []

        while left <= right and top <= bottom:
            #left -> right
            print(left,right)
            
            i = left
            for j in range(left, right+1):
                ans.append(matrix[i][j])

            #right -> bottom
            j = right
            for i in range(top+1, bottom+1):
                ans.append(matrix[i][j])

            #bottom ->left
            i = bottom
            if top < bottom:
                for j in range(right-1, left-1,-1):
                        ans.append(matrix[i][j])

            #left -> top
            j = left
            if left < right:
                for i in range(bottom-1,top,-1):
                    ans.append(matrix[i][j])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return ans






        