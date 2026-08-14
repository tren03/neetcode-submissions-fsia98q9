# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return 0

        # we need to calc the cur_max 
        def rec(root,cur_max):
            if root is None:
                return 
            # root has val to check
            if root.val >= cur_max:
                self.ans += 1
            rec(root.right, max(cur_max,root.val))
            rec(root.left, max(cur_max,root.val))

        rec(root,root.val-1)
        return self.ans



        