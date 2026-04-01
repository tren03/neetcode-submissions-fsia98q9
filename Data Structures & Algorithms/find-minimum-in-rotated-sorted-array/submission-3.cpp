class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size()-1;
        int ans = INT_MAX;

        while(r>=l)
        {
            
            int mid = (l+r)/2;
            cout<<nums[mid]<<endl;
            ans = min(ans,nums[mid]);
            if(nums[l]<nums[mid] && nums[mid]<nums[r])
            {
                return nums[l];
            }
            if(nums[mid]>=nums[l])
            {
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }

        }

        return ans;

        
    }
};
