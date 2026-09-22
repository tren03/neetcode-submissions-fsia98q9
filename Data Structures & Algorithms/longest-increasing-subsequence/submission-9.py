class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        dp = [-1] * len(nums)
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            
            ans = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1+dfs(j))
            dp[i] = ans
            return ans
        
        return max(dfs(i) for i in range(len(nums)))
        