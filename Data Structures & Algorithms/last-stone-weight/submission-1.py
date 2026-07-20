import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] # for max heap
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            small = min(-x,-y)
            big = max(-x,-y)
            new_weight = big - small
            heapq.heappush(stones,-new_weight)
        
        if len(stones) == 1:
            return -stones[0]
        return 0

                
            

        