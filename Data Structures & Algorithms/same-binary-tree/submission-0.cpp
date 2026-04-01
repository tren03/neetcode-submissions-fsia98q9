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
    bool dfs(TreeNode* p, TreeNode* q,bool &ans)
    {
        if(ans==false)
        {
            return false;
        }
        if(!p && !q)
        {
            ans = true;
            return true;
        }
        if((p == nullptr && q != nullptr) || (p != nullptr && q == nullptr) || (p->val != q->val))
        {
            ans = false;
            return false;
        }
        else
        {
            dfs(p->left,q->left,ans);
            dfs(p->right,q->right,ans);
        }

        
        

        return ans;
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool ans = true;
        dfs(p,q,ans);
        return ans;
        
        
    }
};
