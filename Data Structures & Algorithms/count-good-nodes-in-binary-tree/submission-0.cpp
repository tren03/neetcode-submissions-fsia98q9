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
    void dfs(TreeNode* root,int m,int &count)
    {
        if(!root)
        {
            return;
        }
        if(root->val >= m)
        {
            m = root->val;
            count++;
        }

        dfs(root->left,m,count);
        dfs(root->right,m,count);

        return;
    }
    int goodNodes(TreeNode* root) {
        int m=INT_MIN;
        int count = 0;
        dfs(root,m,count);
        return count;
        
    }
};
