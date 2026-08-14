class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0


        while i < len(matrix):
            row = matrix[i]

            print(target,row[-1])
            if target > row[-1]:
                i += 1
                continue

            l,r = 0,len(row) - 1
            print("searching row",row)
            while l<=r:
                m_index = (l+r)//2
                m_val = row[m_index]

                if target == m_val:
                    return True
                if target < m_val:
                    r = m_index - 1
                else:
                    l = m_index + 1
            return False

        return False


    

        
        

            
        