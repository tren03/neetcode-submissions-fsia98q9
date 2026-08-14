# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root,sub):
            if root is None and sub is None:
                return True
            if root is not None and sub is None or root is None and sub is not None:
                return False
            if root.val != sub.val:
                return False
            l_check = is_same_tree(root.left,sub.left)
            r_check = is_same_tree(root.right,sub.right)
            return (l_check and r_check)

        if not subRoot:
            return True
        if not root:
            return False
        
        if is_same_tree(root,subRoot):
            return True
        
        l_check = self.isSubtree(root.left,subRoot)
        r_check = self.isSubtree(root.right,subRoot)
        
        return l_check or r_check

            

        
        

            


        