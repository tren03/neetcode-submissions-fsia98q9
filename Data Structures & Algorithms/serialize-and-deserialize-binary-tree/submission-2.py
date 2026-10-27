# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def rec(cur):
            if cur == None:
                return "N"
            left = rec(cur.left)
            right = rec(cur.right)
            return str(cur.val) + "." + left + "." + right
        
        ans = rec(root)
        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split('.')
        # ['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']
        self.i = 0

        def rec():
            if self.i >= len(vals):
                return None
            if vals[self.i] == 'N':
                self.i += 1
                return None
            t = TreeNode(val=int(vals[self.i]))
            self.i += 1
            left = rec()
            right = rec()
            t.left = left
            t.right = right
            return t

        return rec()
