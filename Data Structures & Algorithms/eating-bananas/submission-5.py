class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 0
        for i in piles:
            r = max(i,r)
        print(l,r)
        ans = r

        while l <= r:
            prob_rate = (l+r)//2
            prob_hours = 0
            for i in piles:
                cur_hours = math.ceil(i/prob_rate)
                prob_hours += cur_hours
            
            if prob_hours > h:
                # taking to long, so rate very slow, pls increase rate
                l = prob_rate + 1
            else:
                # too fast, we can afford to slow rate down
                r = prob_rate - 1
                ans = min(ans, prob_rate)

        return ans



        