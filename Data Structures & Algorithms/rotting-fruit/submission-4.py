class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = []
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
            
        while q:
            popped = q[0]
            i = popped[0]
            j = popped[1]
            t = popped[2]

            q = q[1:]

            d = [(1,0),(-1,0),(0,1),(0,-1)]
            for c in d:
                new_i = i + c[0]
                new_j = j + c[1]

                if new_i >= n or new_j >= m or new_i < 0 or new_j < 0:
                    continue
                v = grid[new_i][new_j]
                if v == 1:
                    ans = max(ans,t+1)
                    grid[new_i][new_j] = 2 # mark as rotten
                    q.append((new_i,new_j,t+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return ans
                    









        