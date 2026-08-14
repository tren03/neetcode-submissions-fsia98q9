# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def depth(root) -> int:
            if root == None:
                return 0
            return max(depth(root.left),depth(root.right)) + 1
        
        def rec(root):
            if root == None:
                return
            l_depth = depth(root.left)
            r_depth = depth(root.right)
            self.ans = max(self.ans, l_depth+r_depth)
            rec(root.right)
            rec(root.left)
        
        rec(root)
        return self.ans


        