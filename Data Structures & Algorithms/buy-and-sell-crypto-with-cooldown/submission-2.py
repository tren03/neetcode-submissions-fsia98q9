class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ans = 0
        dp = {}
        
        def rec(i, coin_owned):
            if i >= len(prices):
                return 0
            if dp.get((i, coin_owned)) is not None:
                return dp[(i,coin_owned)]
                
            cur_coin = prices[i]
            if coin_owned is not None:
                a = 0
                b = 0
                # sell
                if cur_coin > coin_owned:
                    profit = cur_coin - coin_owned
                    a = profit + rec(i+2, None)
                # do nothing
                b = rec(i+1, coin_owned)
                dp[(i, coin_owned)] = max(a,b)
                return max(a,b)
            else:
                a = 0
                b = 0
                # last sold case - we skip the day after we sell, as we dont do anything
                # buy coin
                a = rec(i+1,cur_coin)
                # skip coin
                b = rec(i+1, None)
                dp[(i, coin_owned)] = max(a,b)
                return max(a,b)

        
        rec(0, None)
        return max(dp.values())


                



            
            
            
        