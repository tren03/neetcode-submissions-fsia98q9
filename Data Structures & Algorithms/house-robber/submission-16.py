class Solution:
    def rob(self, nums: List[int]) -> int:
        # what does each rec call actaully mean?
        # it means, if i start at this house, what is max i can rob

        # bottom up
        n = len(nums)
        dp = [-1] * (n+1) # this provides us a buffer for i+2 dp call
        dp[-1] = 0
        dp[-2] = nums[-1]

        for i in range(n-2,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        return dp[0]




        


            
            
        


