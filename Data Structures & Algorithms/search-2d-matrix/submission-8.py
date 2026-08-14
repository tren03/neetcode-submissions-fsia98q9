class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # most optimal - o(log nm)
        # 2d - 1d = i * n + j
        # 1d - 2d =   i = x  // n, j = x % n

        n = len(matrix[0])
        m = len(matrix)
        print(m,n)

        l = 0
        r = m*n - 1

        while l <= r:
            m_index = (l+r)//2
            i = m_index // n
            j = m_index % n
            m_val = matrix[i][j]
            print(l,r,m_index,i,j)

            if m_val == target:
                return True
            if m_val > target:
                r = m_index - 1
            else:
                l = m_index + 1
        return False


        