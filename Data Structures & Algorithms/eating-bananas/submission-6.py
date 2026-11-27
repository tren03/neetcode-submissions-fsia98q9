class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,0
        for p in piles:
            r = max(r, p)

        while l <= r:
            # cur hour calc
            mid = (l+r) // 2
            cur_hours = 0
            for p in piles:
                cur_hours += math.ceil(p/mid)
            
            # eating too slow
            if cur_hours > h:
                # increase rate
                l = mid + 1
            else:
                r = mid - 1
        
        return l
                
        
    

            





        