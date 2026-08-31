class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        vis = [False] * len(points)
        heapq.heappush(pq,[0,0])
        res = 0

        while pq:
            popped = heapq.heappop(pq)
            i = popped[1]
            w = popped[0]
            if vis[i]:
                continue
            vis[i] = True
            res += w

            for j in range(len(points)):
                if j == i:
                    continue
                if vis[j]:
                    continue
                p1 = points[i]
                p2 = points[j]
                dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                heapq.heappush(pq,[dist,j])
        return res


            

            
                

        