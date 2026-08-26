class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # something like a dfs? 
        n = len(board)
        m = len(board[0])

        def dfs(i,j,k):
            if k == len(word):
                return True
            if i >= n or j >= m or i < 0 or j < 0:
                return False
            if board[i][j] != word[k]:
                return False
            if board[i][j] == "#": # already visited
                return False
            board[i][j] = "#"
            a = dfs(i+1,j,k+1)
            b = dfs(i-1,j,k+1)
            c = dfs(i,j+1,k+1)
            d = dfs(i,j-1,k+1)
            board[i][j] = word[k]
            return a or b or c or d


        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False

            
            



            
            


        