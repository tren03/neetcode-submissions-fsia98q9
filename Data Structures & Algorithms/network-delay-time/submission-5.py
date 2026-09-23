class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for e in times:
            source = e[0]
            dest = e[1]
            weight = e[2]
            adj[source].append([dest,weight])
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0

        pq = []
        pq.append([0,k]) # (dist_from_source, node)

        while pq:
            popped = pq[0]
            heapq.heappop(pq)
            cur_dist_to_start = popped[0]
            cur_node = popped[1]

            for neigh, weight in adj[cur_node]:
                print(neigh, dist)
                if dist[neigh] > cur_dist_to_start + weight:
                    dist[neigh] = cur_dist_to_start + weight
                    heapq.heappush(pq, [dist[neigh], neigh])
        
        for d in range(1, len(dist)):
            if dist[d] == float('inf'):
                return -1
        return max(dist[1:])
        

        
        