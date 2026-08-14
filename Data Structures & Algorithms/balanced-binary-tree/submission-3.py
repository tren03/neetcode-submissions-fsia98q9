# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def depth(root):
            if self.ans == False:
                return 0
            if root is None:
                return 0
            
            ld = depth(root.left)
            rd = depth(root.right)
            print(ld-rd)
            if abs(ld-rd) > 1:
                self.ans = False
            return max(ld,rd) + 1

        depth(root)
        return self.ans
        