class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo
        # what does each rec call actaully mean?
        # it means, if i start at this house, what is max i can rob
        n = len(nums)
        dp = [-1] * n
        def dfs(cur_house):
            if cur_house >= n:
                # if i am at a house, who is outside range, 
                # max i can rob is 0
                return 0
            if dp[cur_house] != -1:
                return dp[cur_house]
            
            # lets skip this house so i can rob the neighbour
            skip = dfs(cur_house+1)

            # lets rob this house so i rob the next neighbour
            rob = dfs(cur_house+2)

            dp[cur_house] = max(nums[cur_house]+rob, skip)
            return dp[cur_house]
        
        dfs(0)
        
        return dp[0]


            
            
        


