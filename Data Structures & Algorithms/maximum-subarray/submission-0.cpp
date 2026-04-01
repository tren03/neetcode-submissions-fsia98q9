class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int r=0;
        int sum = 0;
        int ans = INT_MIN;
        while(r<nums.size())
        {
            sum += nums[r];
            ans = max(ans,sum);
            if(sum < 0)
            {
                sum = 0;
            }
            
            r++;
            
            
            
        }
        return ans;


    }
};
