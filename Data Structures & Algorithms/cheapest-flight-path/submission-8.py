class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0

        # still dont fully graps
        for i in range(k+1):
            c = cost.copy()
            for edge in flights:
                s = edge[0]
                d = edge[1]
                w = edge[2]

                if cost[s] + w < c[d]:
                    c[d] = cost[s] + w
                
            cost = c.copy()
                
        
        if cost[dst] == float('inf'):
            return -1
        return cost[dst]



            



    

        