class Solution:
    def climbStairs(self, n: int) -> int:
        # memoized soln
        dp = [-1] * n
        def dfs(cur_step):
            if cur_step > n:
                return 0
            if cur_step == n:
                return 1
            if dp[cur_step] != -1:
                return dp[cur_step]
            # take 1 step
            one_step = dfs(cur_step+1)
            two_step = dfs(cur_step+2)
            dp[cur_step] = one_step + two_step
            return one_step + two_step
        return dfs(0)
        







        