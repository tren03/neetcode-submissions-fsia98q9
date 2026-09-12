class Solution:
    def rob(self, nums: List[int]) -> int:
        # what does each rec call actaully mean?
        # it means, if i start at this house, what is max i can rob

        # space optimized
        # our answer depends on only 2 values + nums val dp[i+1], dp[i+2], nums[i]
        n = len(nums)

        b = 0
        a = nums[-1]
        for i in range(n-2,-1,-1):
            cur = max(nums[i]+b, a)
            b = a
            a = cur
        return a







        


            
            
        


