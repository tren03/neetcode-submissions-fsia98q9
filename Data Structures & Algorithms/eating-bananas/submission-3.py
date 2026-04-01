import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_taken(hour_rate,piles):
            hours = 0
            for i in piles:
                hours += math.ceil(i/hour_rate)
            print(hours)
            return hours


        m = 0 
        for i in piles:
            m = max(i,m)
        
        # we get the problable answer range -> [1,m]
        # we can start our binary search
    
        # probable eating rates
        l = 1
        r = m
        
        prob_answer = 0
        while(l<=r):
            m = (r+l)//2
            # check if mid is the correct eating rate

            cur_hours = hours_taken(m,piles)
            if cur_hours == h:
            # hours taken is perfect, we can reduce rate
                prob_anwer = m
                r = m - 1
            
            # hours taken is too much, means we need to increase our eating rate
            if cur_hours > h:
                l = m + 1
            else:
                # hours taken is withinn limit, so we can afford to reduce eating
                prob_answer = m
                r = m - 1

        return prob_answer
    




        