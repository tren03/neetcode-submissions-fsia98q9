class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        ans = 0

        while r < len(prices):
            prof = prices[r] - prices[l]
            if prof < 0:
                l = r
            else:
                ans = max(ans, prof)
                r += 1
                
        return ans




        