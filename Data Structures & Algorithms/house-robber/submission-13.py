class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp = [-1] * len(nums)
#
      #def rec(house):
        #    if house >= len(nums):
        #        return 0
        #    if dp[house] != -1:
        #        return dp[house]
        #    a = nums[house] + rec(house+2)
        #    b = rec(house+1)
        #    dp[house] = max(a,b)
        #    return max(a,b)
#
        #return rec(0)
        if len(nums) <= 2:
            return max(nums)

        a = nums[-1]
        b = max(nums[-2],a)
        for i in range(len(nums)-3,-1,-1):
            x = max(nums[i]+a, b)
            a = b
            b = x
        return b

        

        