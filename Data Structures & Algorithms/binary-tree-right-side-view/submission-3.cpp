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
        vector<int> ans(0,0);
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
            if(ans.size()==level){ans.push_back(0);}
            ans[level] = temp->val;
            if(temp->left)
            {
                q.push({level+1,temp->left});
            }
            

            if(temp->right)
            {
                q.push({level+1,temp->right});
            }
            
        }
        return ans;

        
    }
};
