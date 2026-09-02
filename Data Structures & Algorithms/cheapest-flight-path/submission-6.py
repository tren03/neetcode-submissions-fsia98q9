class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # i dont understand this fully
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(0,k+1):
            temp = dist[:]
            for s,d,w in flights:
                temp[d] = min(dist[s]+w, temp[d])
            dist = temp
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]


        