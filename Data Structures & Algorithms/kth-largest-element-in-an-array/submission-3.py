class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest -> we need to fetch a smaller element from heap head
        # so we use a min heap
        h = []
        heapq.heapify(h)
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
                continue
            if n > h[0]:
                heapq.heappop(h)
                heapq.heappush(h,n)
        return h[0]
            
            
        
        