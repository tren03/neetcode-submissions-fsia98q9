# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def dfs(root, level):
            if root is None:
                return
            if len(self.ans) == level:
                self.ans.append([])
            self.ans[level] = root.val
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return self.ans
            

            
        