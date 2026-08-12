class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.dp = [None] * len(nums)

        def rec(ind):
            if ind >= len(self.nums) - 1:
                return True
                
            if self.dp[ind] is not None:
                return self.dp[ind]
            
            jumps = self.nums[ind]
            for i in range(1,jumps+1):
                self.dp[ind+i] = rec(ind+i)
                if self.dp[ind+i]:
                    self.dp[ind] = True
                    return True

            self.dp[ind] = False
            return False
        
        return rec(0)

        
            

        