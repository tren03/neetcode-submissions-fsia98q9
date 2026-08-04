class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        final_floor = len(cost)
        self.dp = [-1] * final_floor

        def rec(step):
            if step >= final_floor:
                return 0
            if self.dp[step] != -1:
                return self.dp[step]
            self.dp[step] = cost[step] + min(
                rec(step + 1), rec(step + 2)
            )
            return self.dp[step]

        rec(0)
        return min(self.dp[0], self.dp[1])
