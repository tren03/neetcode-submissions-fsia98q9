# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        def rec(root,depth):
            if root is None:
                return
            if len(self.ans) == depth:
                self.ans.append([])
            self.ans[depth].append(root.val)
            rec(root.left,depth+1)
            rec(root.right,depth+1)
        rec(root,0)
        return self.ans
            


        