class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        def f(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            l = f(i+2) + nums[i]
            r = f(i+1)
            dp[i] = max(l,r)
            return max(l,r)

        return f(0)