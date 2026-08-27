# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = float("-inf")
        
        def rec(root):
            if not root:
                return float("-inf")

            left = rec(root.left)
            right = rec(root.right)
            cur = root.val

            a = cur+left+right
            b = cur+left
            c = cur+right
            d = cur
            self.ans = max(self.ans, max(a,b,c,d))
            return max(b,c,d)

        rec(root)
        return self.ans



    
        