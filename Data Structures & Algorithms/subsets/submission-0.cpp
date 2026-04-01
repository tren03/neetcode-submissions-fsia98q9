class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
       vector<vector<int>> ans;
       int ind = 0;
       vector<int> temp = {};
       int f_size = nums.size()-1;

       rec(nums,ind,ans,temp);
       return ans;

    }

    void rec(vector<int>& nums,int ind,vector<vector<int>> &ans,vector<int> t){   
        if (ind == nums.size()){
            ans.push_back(t);
            return;
        }
        t.push_back(nums[ind]);
        ind++;
        rec(nums,ind,ans,t);
        t.pop_back();
        rec(nums,ind,ans,t);
    }


};
