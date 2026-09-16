class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        dp = {}
        def dfs(rem_amt):
            if rem_amt == 0:
                dp[rem_amt] = 0
                return 0
            if rem_amt < 0:
                return float('inf')
            if dp.get(rem_amt) is not None:
                return dp[rem_amt]
                
            dp[rem_amt] = float('inf')
            for i in range(len(coins)):
                dp[rem_amt] = min(dp[rem_amt],1+dfs(rem_amt-coins[i]))
            return dp[rem_amt]
            
        dfs(amount)
        if dp.get(amount) is not None and dp[amount] != float('inf'):
            return dp[amount]
        return -1
        