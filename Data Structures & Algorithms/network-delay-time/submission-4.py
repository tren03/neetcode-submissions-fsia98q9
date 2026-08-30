class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adj
        adj = defaultdict(list)
        for t in times:
            source = t[0]
            dest = t[1]
            weight = t[2]
            adj[source].append((dest,weight))

        dist = [float('inf')] * n
        # seed initial elements
        dist[k-1] = 0
        mheap = [[0,k]]
        heapq.heapify(mheap)
        

        while mheap:
            popped = heapq.heappop(mheap)
            weight = popped[0]
            source = popped[1]
            recorded_weight = dist[source-1]
            if recorded_weight < weight:
                continue
            dist[source-1] = weight
            for neigh in adj[source]:
                if weight+neigh[1] < dist[neigh[0]-1]:
                    dist[neigh[0]-1] = weight+neigh[1]
                    heapq.heappush(mheap,[weight+neigh[1],neigh[0]])

        m = float('-inf')
        for i in dist:
            if i == float('inf'):
                return -1
            m = max(m,i)
        return m

            
            

        


        




        return -1

        