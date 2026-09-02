class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k = k + 1
        ans = float('inf')

        # create adj
        adj = defaultdict(list)
        for e in flights:
            adj[e[0]].append([e[1],e[2]])

        def dfs(node,cur_steps,cur_cost):
            nonlocal ans
            if cur_steps == k and node != dst:
                return
            if cur_steps <= k and node == dst:
                ans = min(ans,cur_cost)
                return
            if cur_cost > ans:
                return
            for neigh in adj[node]:
                neigh_node = neigh[0]
                neigh_weight = neigh[1]
                dfs(neigh_node,cur_steps+1,cur_cost+neigh_weight)


        dfs(src,0,0)
        if ans == float('inf'):
            return -1
        return ans

            
            
            


        