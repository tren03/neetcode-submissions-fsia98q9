# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None

        def rec(root,p,q):
            if root is None:
                return
            v = root.val
            print(root.val,p.val,q.val)
            if p.val <= v and q.val >= v or p.val >= v and q.val <= v:
                self.ans = root
                return
            if p.val <= v and q.val <= v:
                rec(root.left,p,q)
            else:
                rec(root.right,p,q)

        rec(root,p,q)
        print(self.ans)
        return self.ans
            

        