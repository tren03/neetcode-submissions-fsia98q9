class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0;
        int r = n-1;

        while(r>=l)
        {
            int mid = (l+r)/2;
            cout<<nums[mid]<<endl;
            if(nums[mid]==target)
            {
                return mid;
            }

            if(nums[l]<=nums[mid] && nums[mid]<=nums[r])
            {
                //normal binary search
                int li = l;
                int ri = r;
                while(li<=ri)
                {
                    int mid_i = (li+ri)/2;

                if(nums[mid_i]==target)
                {
                    return mid_i;
                }
                else if(target<nums[mid_i])
                {
                    ri = mid_i-1;

                }
                else
                {
                    li = mid_i+1;
                }
                    
                }
                
            }

            // in left sorted array
            if(nums[l]<=nums[mid])
            {
                if(target<nums[l])
                {
                    l = mid+1;
                }
                else
                {
                    r = mid-1;
                }
            }

            else
            {
                if(target>nums[r])
                {
                    r = mid - 1;
                }
                else
                {
                    if(target<mid)
                    {
                        r = mid-1;
                    }
                    else
                    {
                        l = mid+1;
                    }
                
                }
            }

        }
        return -1;
        
    }
};
