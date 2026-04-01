import sys
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # we can start from 0th or 1st index
        dp = {}
        def f(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            l = f(i+1) + cost[i]
            r = f(i+2) + cost[i]
            dp[i] = min(l,r)
            return min(l,r)

        return min(f(0),f(1))



        