class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0

        answer = 0
        while sell<len(prices):
            current_profit = prices[sell] - prices[buy]
            if current_profit < 0:
                buy+=1
                sell = buy
            else:
                sell+=1
            answer = max(current_profit,answer)
        return answer




            


            





        