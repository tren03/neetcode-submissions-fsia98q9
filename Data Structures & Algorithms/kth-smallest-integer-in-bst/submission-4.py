# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # max heap of size k? - then k.top - would give kth smallest

        maxheap = [] # size = k

        def rec(root):
            if not root:
                return
            
            v = root.val
            if len(maxheap) < k:
                heapq.heappush(maxheap,-v)
            else:
                if v >= -maxheap[0]:
                    pass
                else:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap,-v)
            rec(root.left)
            rec(root.right)
        rec(root)
        return -maxheap[0]

            
            
        


        