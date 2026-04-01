class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l =0;
        int r= heights.size()-1;
        int m = INT_MIN;
        while(l<r)
        {
            int temp_area = (r-l)*min(heights[l],heights[r]);
            if(heights[l]<heights[r])
            {
                l++;
            }
            else{
                r--;
            }
            m = max(m,temp_area);

        }
        return m;
    }
};
