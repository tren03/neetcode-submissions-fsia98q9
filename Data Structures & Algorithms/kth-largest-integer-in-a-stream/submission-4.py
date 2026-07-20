import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for v in nums:
            if len(self.pq) < k:
                heapq.heappush(self.pq, v)
            else:
                if v > self.pq[0]:
                    heapq.heappop(self.pq)
                    heapq.heappush(self.pq, v)
        print(self.pq)
        


    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
                heapq.heappush(self.pq, val)
        else:
            if val > self.pq[0]:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, val)
        return self.pq[0]
        
        
