class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def rec(step):
            if step == n:
                return 1
            if step > n:
                return 0
            if dp[step] != -1:
                return dp[step]

            a = rec(step+1)
            b = rec(step+2)

            dp[step] = a+b
            return a+b
        return rec(0)

        