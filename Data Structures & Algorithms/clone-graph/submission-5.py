"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.m = {}
        def rec(node):
            if not node:
                return None
            if node.neighbors is None:
                cloned = Node(node.val)
                self.m[node] = cloned
                return cloned

            cloned = Node(node.val)
            cloned_neigh = []
            self.m[node] = cloned
            for neigh in node.neighbors:
                # try fetching from map, if not exists recurse
                cn = self.m.get(neigh)
                if not cn:
                    cn = rec(neigh)
                cloned_neigh.append(cn)
            cloned.neighbors = cloned_neigh
            self.m[node] = cloned
            return cloned
        return rec(node)





            


        