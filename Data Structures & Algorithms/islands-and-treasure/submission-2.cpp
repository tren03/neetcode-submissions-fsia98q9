class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        // instead of doing bfs twice, we can just push gates into the queue and do bfs for both
        int m = grid.size();
        int n = grid[0].size();
        
        queue<pair<int, int>> q;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        int drow[] = {1,0,-1,0};
        int dcol[] = {0,1,0,-1};

        while(!q.empty())
        {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            for(int i=0;i<4;i++)
            {
                int nrow = row + drow[i];
                int ncol = col + dcol[i];

                if(nrow>=0 && ncol>=0 && nrow<m && ncol<n && grid[nrow][ncol]==INT_MAX)
                {
                    grid[nrow][ncol] = grid[row][col]+1;
                    q.push({nrow,ncol});
                }
            }
        }



        
    }
};
