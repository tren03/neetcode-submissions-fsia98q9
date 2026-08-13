class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m1 = set()
        m2 = set()
        m3 = set()


        for i in range(0,9):
            m1 = set()
            m2 = set()
            for j in range(0,9):
                row_val = board[i][j]
                col_val = board[j][i]

                if row_val in m1:
                    return False
                if col_val in m2:
                    return False

                if row_val != ".":
                    m1.add(row_val)
                if col_val != ".":
                    m2.add(col_val)
        
        temp = [m1,m2,m3]
        # refesh temp
        for i in range(0,3):
            temp[i] = set()
            
        
        # diagonal check
        for i in range(0,9):
            for j in range(0,9):
                val = board[i][j]
                if i % 3 == 0 and j == 0:
                    temp[0] = set()
                    temp[1] = set()
                    temp[2] = set()
                set_to_check = temp[j//3]
                if val in set_to_check:
                    return False
                
                if val != ".":
                    temp[j//3].add(val)

        return True
                
                



                




        