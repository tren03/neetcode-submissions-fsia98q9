class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 0

        while r < len(prices):
            print(l,r)
            t = prices[r] - prices[l]
            if t >= 0:
                profit = max(t, profit)
            else:
                l += 1
                r = l
            r += 1

        return profit


        