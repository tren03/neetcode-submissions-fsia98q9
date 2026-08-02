class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parents = [i for i in range(0,n)]
        size = [1 for i in range(0,n)]

        # logic is - for each edge
        # if rep root of both nodes of edge is diff - merge nodes
        # else return the value - as both nodes belong to same connected graph
        # so adding this edge makes it a cycle
        def find(node):
            p1 = parents[node]
            p2 = parents[p1]
            while p1 != p2:
                p1 = p2
                p2 = parents[p2]
            return p1

        def union(p1,p2):
            # merge components using their rep root
            # fetch size of parents
            p1_size = size[p1]
            p2_size = size[p1]
            if p1_size < p2_size:
                # 2 is root
                parents[p2] = p1
            else:
                # 1 is root
                parents[p1] = p2



        print(parents)
        for e1, e2 in edges:
            p1, p2 = find(e1), find(e2)
            if p1 == p2:
                return [e1,e2]
            union(p1,p2)

