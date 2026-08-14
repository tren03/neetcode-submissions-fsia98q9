class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = []
        for i in range(0,n):
            vis.append([])
            for j in range(0,m):
                vis[i].append(False)
        self.grid = grid
        self.ans = 0
        self.count = 0
        
        def dfs(i,j,vist):
            if i >= n or j >= m or i < 0 or j < 0:
                return
            if self.grid[i][j] == 0 or vis[i][j] == True:
                return
            # grid[i][j] is 1 and not visited
            vis[i][j] = True
            self.count += 1
            self.ans = max(self.ans,self.count)
            dfs(i+1,j,vis)
            dfs(i-1,j,vis)
            dfs(i,j+1,vis)
            dfs(i,j-1,vis)
        
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 1 and vis[i][j] == False:
                    self.count = 0
                    dfs(i,j,vis)
        return self.ans




        