class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        initially we have n components
        when we come across a edge - we can do dfs on the edge
        and all edges reached from that edge - 1 component.
        if any edges not reached, then we do dfs from them as well
        total count -> answer
        """
        def dfs(i,vis):
            if vis[i] == True:
                return
            vis[i] = True
            children = adj[i]
            for t in children:
                dfs(t,vis)
                
        ans = 0
        adj = defaultdict(list)
        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        vis = [False] * n
        for i in range(n):
            if vis[i] == False:
                ans +=1
                dfs(i,vis)
        return ans


            



        