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
    void dfs(TreeNode*root, bool &ans,int min,int max)
    {
        if(!root || !ans)
        {
            return;
        }
        if(root->val <= min || root->val >= max)
        {
            ans = false;
            return;
        }

        dfs(root->left,ans,min,root->val);
        dfs(root->right,ans,root->val,max);
        return;
        
        
    }
    bool isValidBST(TreeNode* root) {
        bool ans = true;
        dfs(root,ans,INT_MIN,INT_MAX);
        return ans;
        
        
    }
};
