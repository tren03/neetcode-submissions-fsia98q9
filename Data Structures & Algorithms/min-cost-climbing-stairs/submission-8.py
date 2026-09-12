class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo
        if len(cost) == 1:
            return cost[0]
        n = len(cost)
        dp = [-1] * n
        def dfs(cur_step):
            if cur_step >= n:
                return 0
            if dp[cur_step] != -1:
                return dp[cur_step]
            dp[cur_step] = cost[cur_step] + min(dfs(cur_step+1),dfs(cur_step+2))
            return dp[cur_step]
        return min(dfs(0),dfs(1))




        