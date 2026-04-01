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
    bool dfs(TreeNode* p, TreeNode* q, bool &ans)
    {
        if((p == nullptr && q != nullptr) || (p != nullptr && q == nullptr) || ((p&&q) && (p->val != q->val)) || !ans)
        {
            ans = false;
            return false;
        }        
        if((!p&&!q))
        {
            return true;
        }
        
        
        dfs(p->right,q->right,ans);
        dfs(p->left,q->left,ans);

        return ans;
    }
    
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root && !subRoot)
        {
            return false;
        }
        stack<TreeNode*> st;
        st.push(root);
        
        while(!st.empty())
        {
            bool ans = true;
            TreeNode* temp = st.top();
            st.pop();
            ans = dfs(temp,subRoot,ans);
            cout<<(ans);
            if(ans==true)
            {
                return true;
            }
            if(temp->right) { st.push(temp->right);}
            if(temp->left) {st.push(temp->left);}

        }
        return false;
        
        
        
        
    }
};
