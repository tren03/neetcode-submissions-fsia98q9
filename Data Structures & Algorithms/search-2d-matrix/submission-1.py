class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #have a func and 1d_to_2d, 
        # do binary search in 1D, but access elements through 2D only

        rows = len(matrix)
        cols = len(matrix[0])

        def convert(index) -> int:
            j = index % cols
            i = (index // cols) 
            return i,j

        r = (rows * cols) - 1
        l = 0

        while(l<=r):
            mid = (l+r)//2
            i,j = convert(mid)
            nos = matrix[i][j]
            if nos == target:
                return True
            
            if nos > target:
                r = mid - 1
            else:
                l = mid + 1
            

        return False
            
            


        