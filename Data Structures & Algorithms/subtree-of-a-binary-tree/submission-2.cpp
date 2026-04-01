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
    bool check(TreeNode* p, TreeNode* q)
    {
        if((p == nullptr && q != nullptr) || (p != nullptr && q == nullptr) || ((p&&q) && (p->val != q->val)))
        {
            
            return false;
        }        
        if((!p&&!q))
        {
            return true;
        }       
        bool left = check(p->left,q->left);
        bool right = check(p->right,q->right);
        if(left==false || right==false)
        {
            return false;
        }
        return true;
    }
    
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!subRoot)
        {
            return true;
        }

        if(!root)
        {
            return false;
        }

        bool cur = check(root,subRoot);
        bool left = isSubtree(root->left,subRoot);
        bool right = isSubtree(root->right,subRoot);


        if(cur||left||right)
        {
            return true;
        }
        return false;
        
        
        
        
    }
};
