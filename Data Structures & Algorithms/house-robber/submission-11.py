class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def rec(house):
            if house >= len(nums):
                return 0
            if dp[house] != -1:
                return dp[house]
            a = nums[house] + rec(house+2)
            b = rec(house+1)
            dp[house] = max(a,b)
            return max(a,b)

        return rec(0)


        

        