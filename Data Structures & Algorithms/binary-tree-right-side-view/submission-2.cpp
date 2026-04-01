/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<vector<int>> view;
        queue<pair<int,TreeNode*>> q;
        if(!root)
        {
            return {};
        }
        q.push({0,root});
        while(!q.empty())
        {
            TreeNode* temp = q.front().second;
            int level = q.front().first;
            q.pop();
            if(view.size()==level)
            {
                view.push_back(vector<int>());
            }
            view[level].push_back(temp->val);
            if(temp->left)
            {
                q.push({level+1,temp->left});
            }
            

            if(temp->right)
            {
                q.push({level+1,temp->right});
            }
            
        }
        vector<int> ans;
        for(int i=0;i<view.size();i++)
        {
            for(auto j:view[i])
            {
                cout<<j;
            }
            cout<<endl;
            ans.push_back(view[i][view[i].size()-1]);
        }
        return ans;

        
    }
};
