class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[-1] = 1
        dp[-2] = 1
        for i in range(n-1,-1,-1):
            print(dp,i)
            dp_2 = 0
            if i+2 <= n:
                dp_2 = dp[i+2]
            dp[i] = dp[i+1] + dp_2
        return dp[0]
        