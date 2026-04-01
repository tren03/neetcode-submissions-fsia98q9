class Solution {
public:
    bool pacific_check(int r,int c,int m,int n)
    {
        if((r==0 && c<n && c>=0) || (c==0 && r<m && r>=0))
        {
            return true;
        }
        return false;
    }
    bool atl_check(int r,int c,int m,int n)
    {
        if((r==m-1 && c<n && c>=0) || (c==n-1 && r<m && r>=0))
        {
            return true;
        }
        return false;
    }
    void dfs(int r,int c,int m,int n,vector<vector<int>>& heights,vector<vector<int>> &ans)
    {
        // for every cell, do dfs and check if it reached both pacific node and atl node,
        // if yes append the pair to and vector

        stack<pair<int,int>> st;
        st.push({r,c});
        int drow[] = {0,1,0,-1};
        int dcol[] = {-1,0,1,0};
        pair<int,int> temp(0,0);
        vector<vector<int>> vis(m,vector<int>(n,0));

        if(pacific_check(r,c,heights.size(),heights[0].size()) && temp.first!=1)
        {
            temp.first = 1;
        }
        if(atl_check(r,c,heights.size(),heights[0].size()) && temp.second!=1)
        {
            temp.second = 1;
        }
        

        while(!st.empty())
        {
            int row = st.top().first;
            int col = st.top().second;
            vis[row][col] = 1;
            st.pop();

            for(int i = 0;i<4;i++)
            {
                int nr = row+drow[i];
                int nc = col+dcol[i];

                if(nc>=0 && nr>=0 && nc<n && nr<m && vis[nr][nc]==0 && heights[nr][nc]<=heights[row][col])
                {
                    if(pacific_check(nr,nc,heights.size(),heights[0].size()) && temp.first!=1)
                    {
                        temp.first = 1;
                    }
                    if(atl_check(nr,nc,heights.size(),heights[0].size()) && temp.second!=1)
                    {
                        temp.second = 1;
                    }
                    st.push({nr,nc});
                }
                
            }
        
        }

        if(temp.first && temp.second)
        {
            ans.push_back({r,c});
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {

        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> ans;

        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                dfs(i,j,m,n,heights,ans);
            }
        }

        return ans;


        

        
    }
};
