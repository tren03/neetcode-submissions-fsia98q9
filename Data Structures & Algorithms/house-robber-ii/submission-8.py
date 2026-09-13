class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [-1] * n

        def dfs(cur,l):
            if cur >= l:
                return 0
            if dp[cur] != -1:
                return dp[cur]
            dp[cur] = max(nums[cur] + dfs(cur+2,l), dfs(cur+1,l))
            return dp[cur]

        a = dfs(0,n-1)
        dp = [-1] * n
        b = dfs(1,n)
        return max(a,b)
        





