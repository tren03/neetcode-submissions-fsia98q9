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
    int dfs(TreeNode* root,bool &ans)
    {
        if(root==nullptr)
        {
            return 0;
        }
        int right = dfs(root->right,ans);
        int left = dfs(root->left,ans);
        if((left-right)>1 ||(right-left)>1)
        {
            ans = false;
        }
        return 1+max(left,right);
    }
    bool isBalanced(TreeNode* root) {
        bool ans = true;
        dfs(root,ans);
        return ans;
        
        
    }
};
