class Solution {
public:
    void initialize_vis(int m,int n,vector<vector<int>> &vis,vector<vector<int>> &grid)
    {
        for(int i = 0;i<m;i++)
        {   
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]>1)
                {
                    vis[i][j] =0; // unvisited
                }
                else
                {
                    vis[i][j] =-1; // cannot visit
                }
            }
        }
    }

    void bfs(int m,int n, int i,int j, vector<vector<int>>& grid,vector<vector<int>>& vis)
    {   
        queue<pair<int,int>> q;
        q.push({i,j});
        int count = 1;
        int drow[] = {1,0,-1,0};
        int dcol[] = {0,1,0,-1};
        vis[i][j] = -1;
        while(!q.empty())
        {
             
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            for(int i=0;i<4;i++)
            {
                    int nrow = row+drow[i];
                    int ncol = col+dcol[i];
                    if(nrow<m && ncol<n && nrow>=0 && ncol>=0 && grid[nrow][ncol]>1 && vis[nrow][ncol] == 0)
                    { 
                        q.push({nrow,ncol});
                        grid[nrow][ncol] = min(grid[nrow][ncol],grid[row][col]+1);
                        vis[nrow][ncol] = -1;
                    }
            }
            

        }


        

    }
    void islandsAndTreasure(vector<vector<int>>& grid) {

    // do bfs for every gate, update value if val is smaller

    //creating a vis vector
    



    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> vis(m, vector<int>(n, 0));

    for(int i = 0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(grid[i][j]==0)
            {
                initialize_vis(m,n,vis,grid);
                bfs(m,n,i,j,grid,vis);
            }
        }
    }



        
    }
};
