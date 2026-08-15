class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        q = []

        # multisource bfs
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        

        while q:
            popped = q[0]
            i = popped[0]
            j = popped[1]
            depth = popped[2]
            q = q[1:]

            # next nodes to visit
            d = [(1,0),(-1,0),(0,1),(0,-1)]

            for c in d:
                new_i = i + c[0]
                new_j = j + c[1]

                if new_i >= n or new_j >= m or new_i < 0 or new_j < 0:
                    continue
                v = grid[new_i][new_j]
                if v == 2147483647: 
                    grid[new_i][new_j] = depth + 1
                    q.append((new_i,new_j,depth+1))



        