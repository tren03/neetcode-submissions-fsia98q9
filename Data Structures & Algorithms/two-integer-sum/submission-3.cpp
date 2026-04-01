class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> st;
        for(int i=0;i<nums.size();i++){
            if(st.find(nums[i])==st.end()){
                st[nums[i]] = i; 
            }
        }
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            auto it = st.find(target-nums[i]);
            if(st.find(target-nums[i])!=st.end() && i!=it->second){
                auto it = st.find(target-nums[i]);
                ans.push_back(i);
                ans.push_back(it->second); 
                break;
                         
            }
        }
        sort(ans.begin(),ans.end());
        return ans;
        
    }
};
