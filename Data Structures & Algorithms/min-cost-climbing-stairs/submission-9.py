class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up
        n = len(cost)
        dp = [-1] * (n+1)
        dp[-1] = 0
        dp[-2] = cost[-1]

        for i in range(n-2,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        
        return min(dp[0],dp[1])



        