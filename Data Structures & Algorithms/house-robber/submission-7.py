class Solution:
    def rob(self, nums: List[int]) -> int:
        # lets optimize this
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]


        dp = [0] * n 
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2],nums[-1])
        for i in range(n-3,-1,-1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        return dp[0]




