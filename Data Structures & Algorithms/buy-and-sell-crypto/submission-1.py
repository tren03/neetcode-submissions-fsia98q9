class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brure force is easy, 2 for loops
        l,r = 0,0
        ans = 0
        while(r<len(prices)):
            if prices[r]<prices[l]:
                ans = max(ans,prices[r]-prices[l])
                l = r
            else:
                ans = max(ans,prices[r]-prices[l])
            r+=1
        return ans



        