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
    void traversal(TreeNode*root, TreeNode*p,TreeNode*q,TreeNode* &ans)
    {
        
        if(p->val == root->val || q->val==root->val)
        {
            if(p->val == root->val)
            {
                ans = p;
            }
            else
            {
                ans = q;
            }
        }
        if((p->val < root->val && q->val > root->val) || (q->val < root->val && p->val > root->val))
        {
            ans = root;
        }
        if(p->val > root->val && q->val > root->val)
        {
            traversal(root->right,p,q,ans);
        }
        if(p->val < root->val && q->val < root->val)
        {
            traversal(root->left,p,q,ans);
        } 

        return;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* ans = new TreeNode(101);
        traversal(root,p,q,ans);
        return ans;
        

        
    }
};
