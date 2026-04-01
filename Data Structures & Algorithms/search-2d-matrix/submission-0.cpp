class Solution {
public:
    int to1D(int i,int j,int n)
    {
        return (i*n)+j;
    }
    pair<int,int> to2D(int temp,int n)
    {
        pair<int,int> t;
        t.first = temp/n;
        t.second = temp%n;
        return t;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        int l = to1D(0,0,n);
        int r = to1D(m-1,n-1,n);
        while(r>=l)
        {
            int mid = (l+r)/2;
            pair<int,int> temp = to2D(mid,n);
            
            int i = temp.first;
            int j = temp.second;
            cout<<i<<j<<endl;
            if(matrix[i][j] == target)
            {
                return true;
            }
            else if(matrix[i][j] < target)
            {
                l = mid+1;
            }
            else
            {
                r = mid-1;
            }
        }
        return false;


        

        
    }
};
