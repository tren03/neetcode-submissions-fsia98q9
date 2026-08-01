class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [False] * n
        # create adj
        adj = {}
        for node in range(0,n):
            adj[node] = []

        for edge in edges:
            e1 = edge[0]
            e2 = edge[1]
            adj.setdefault(e1,[]).append(e2)
            adj.setdefault(e2,[]).append(e1)
        

        def dfs(node, vis):
            if vis[node]:
                return
            vis[node] = True
            for neigh in adj[node]:
                if not vis[neigh]: # not visited, so we do not revisit
                    dfs(neigh, vis)
        
        ans = 0
        for node in range(0,n):
            if not vis[node]: # not been visited
                ans += 1
                dfs(node, vis)

        return ans

        


                
                

            




        
        