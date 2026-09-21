class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        # i is cur element, j is last chosen
        dp = {}
        def dfs(i,j):
            if i >= len(nums):
                return 0
            if dp.get((i,j)):
                return dp[(i,j)]
            cur = nums[i]
            a = 0
            b = 0
            if cur > j:
                a = dfs(i+1, cur) + 1
            b = dfs(i+1, j)
            dp[(i,j)] = max(a,b)
            return max(a,b)
        return dfs(0,float('-inf'))
            


                
            
        