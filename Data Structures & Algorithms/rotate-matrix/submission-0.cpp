class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // find transpose, swap the columns

        //finding transpose

        for(int i=0;i<matrix.size();i++)
        {
            for(int j=i;j<matrix[0].size();j++)
            {
                swap(matrix[i][j],matrix[j][i]);
            }
        }

        int i=0;
        int j=matrix.size()-1;
        while(j>i)
        {
            for(int itr1 = 0;itr1<matrix.size();itr1++)
            {
                swap(matrix[itr1][i],matrix[itr1][j]);
            }
            j--;
            i++;

        }


        
    }
};
