class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        print(dp)
        
        def rec(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            
            m = float('inf')
            for i in coins:
                if rem-i < 0:
                    continue
                if dp[rem-i] is not None and dp[rem-i] != 1:
                    c = dp[rem-i]
                else:
                    c = rec(rem-i)
                if c == -1:
                    continue
                m = min(m,c+1)
            print(rem)
            dp[rem] = m
            return dp[rem]

        a = rec(amount)
        if a != float('inf'):
            return a
        return -1

        

            
        