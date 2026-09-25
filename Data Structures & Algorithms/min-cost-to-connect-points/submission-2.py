class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        cost = 0
        vis = set()

        heapq.heappush(pq, (0,(points[0][0], points[0][1])))

        while pq:
            popped = heapq.heappop(pq)
            cur = popped[1]
            if cur in vis:
                continue
            cost += popped[0]
            vis.add((cur[0], cur[1]))

            for n in points:
                if n == cur:
                    continue
                neigh = n
                cur_dist = abs(cur[0]-neigh[0]) + abs(cur[1]-neigh[1])
                heapq.heappush(pq, (cur_dist, (neigh[0], neigh[1])))
        return cost

                


        

            



        