class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        if n == 1:
            return 1

        dp = [-1] * (n+1)
        dp[-1] = 1
        dp[-2] = 1

        for i in range(n-2,-1,-1):
            print(dp[i+1],dp[i+2])
            dp[i] = dp[i+1] + dp[i+2]
            print(dp[i])
        return dp[0]
                



         







        