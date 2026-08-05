class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.n = len(nums)
        self.dp = [None] * n

        def rec(house_number, end):
            if self.n == 1:
                return nums[0]
            if house_number >= end:
                return 0
            if self.dp[house_number]:
                return self.dp[house_number]
            
            self.dp[house_number] = max(
            rec(house_number+2, end) + nums[house_number],
            rec(house_number+1, end)
            )
            return self.dp[house_number]
        
        a = rec(0,n-1)
        self.dp = [None] * n
        b = rec(1,n)
        return max(a,b)





            
            

            
        