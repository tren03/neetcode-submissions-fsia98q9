class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        q = []

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == n-1 or j == m-1):
                    # only if in border and 0, mark visited, and add to q
                    board[i][j] = 1
                    q.append((i,j))
        
        
        while q:
            popped = q[0]
            q = q[1:]
            i = popped[0]
            j = popped[1]

            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for c in d:
                ni = i + c[0]
                nj = j + c[1]

                if ni >= n or nj >= m or ni < 0 or nj < 0:
                    continue
                v = board[ni][nj]
                if v == "O":
                    # not visited,
                    q.append((ni,nj))
                    board[ni][nj] = 1

        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        




        