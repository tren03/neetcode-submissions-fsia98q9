import heapq
def dist(x,y) -> float:
    return math.sqrt(math.pow((x),2)+math.pow((y),2))

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap of len k to store the kth closest
        distances = [] # list[tuple(float, int, [int,int])]

        i = 0
        for point in points:
            d = dist(point[0],point[1])
            temp = (-d, i, point)
            distances.append(temp)

        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        
        ans = []
        for a,b,c in distances:
            ans.append(c)
            
        return ans




        