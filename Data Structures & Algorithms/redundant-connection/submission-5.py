class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        state = [i for i in range(n+1)]
        print(state)

        def find(node):
            while state[node] != node:
                node = state[node]
            return node

        def union(parent, child):
            p = find(parent)
            c = find(child)
            if p == c:
                return [parent,child]
            # merge otherwise since they are part of diff groups
            state[c] = p

        for e in edges:
            ans = union(e[0],e[1])
            if ans:
                return ans

        return []

