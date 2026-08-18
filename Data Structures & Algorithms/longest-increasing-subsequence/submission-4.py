class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * len(nums) 

        def rec(i):
            if i == 0:
                dp[0] = 1
                return 1
            if dp[i] != -1:
                return dp[i]

            m = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    m = max(rec(j),m)
            dp[i] = m + 1
            return m + 1
        

        for i in range(len(nums)):
            rec(i)
        return max(dp)


            
        