class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # # memoizations
        # dp = {}
        # def f(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in dp:
        #         return dp[i]
            
        #     l = f(i+2) + nums[i]
        #     r = f(i+1)
        #     dp[i] = max(l,r)
        #     return max(l,r)

        # return f(0)

        # tabulation
        dp = [-1] * len(nums)
        if len(nums) ==1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            l = dp[i-2] + nums[i]
            r = dp[i-1]
            dp[i] = max(l,r)
        return dp[-1]


        