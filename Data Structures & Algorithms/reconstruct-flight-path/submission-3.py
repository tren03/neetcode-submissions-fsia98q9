class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)
        
        for n in adj.keys():
            adj[n].sort(reverse=True)

        ans = []

        def rec(node):
            # if there are dest to visit, visit
            while adj[node]:
                # pop the element to visit
                pp = adj[node].pop()
                rec(pp)
            
            ans.append(node)
        
        rec("JFK")
        ans.reverse()
        return ans

                
        

        