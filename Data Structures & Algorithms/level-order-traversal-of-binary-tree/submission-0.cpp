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
    vector<vector<int>> levelOrder(TreeNode* root) {
        unordered_map<int,vector<TreeNode*>> ans;
        queue<pair<int,TreeNode*>> q;
        if(!root)
        {
            return {};
        }
        q.push({0,root});
        while(!q.empty())
        {
            TreeNode *temp = q.front().second;
            int level = q.front().first;
            ans[level].push_back(temp);
            q.pop();
            if(temp->left)
            {
                q.push({level+1,temp->left});
            }
            if(temp->right)
            {
                q.push({level+1,temp->right});
            }
        }
        vector<vector<int>> a(ans.size());
        for(int i = 0; i<ans.size();i++)
        {
            vector<TreeNode*> l = ans[i]; // refers to the vector of treenodes of level i
            for(auto j:l)
            {
                cout<<j->val;
                a[i].push_back(j->val);
            }
            cout<<endl;
        }
        return a;
        
    }
};
