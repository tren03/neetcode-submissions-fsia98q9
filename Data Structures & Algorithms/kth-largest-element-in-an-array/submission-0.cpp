class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int>> p;

        for(auto i:nums)
        {
            if(p.size()==k)
            {
                if(i>p.top())
                {
                    p.pop();
                    p.push(i);
                }
            }
            else
            {
                p.push(i);
            }
        }
        return p.top();

        
    }
};
