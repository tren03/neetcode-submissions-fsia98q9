# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def rec(root,left,right):
            if self.ans == False:
                return

            if root is None:
                return None

            v = root.val
            if v <= left or v >= right:
                self.ans = False
                return
            
            rec(root.left,left,root.val)
            rec(root.right,root.val,right)
        rec(root,-1000000000,1000000000)

        return self.ans



        