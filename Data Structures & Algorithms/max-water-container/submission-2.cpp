class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size()-1;
        int m = INT_MIN;
        while(l<r){
            int area = (r-l) * min(heights[r],heights[l]);
            
            m = max(area,m);
            cout<<m<<endl;

            if(heights[l]<=heights[r]){
                l++;               
            }else{
                r--;
            }
        }

        return m;
        
    }
};
