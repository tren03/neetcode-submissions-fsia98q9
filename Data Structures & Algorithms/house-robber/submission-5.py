class Solution:
    def rob(self, nums: List[int]) -> int:
        # lets optimize this
        self.dp = [-1] * (len(nums))

        def rec(house_number):
            if house_number >= len(nums):
                return 0
            if self.dp[house_number] != -1:
                return self.dp[house_number]

            cost_to_rob = nums[house_number]
            self.dp[house_number] = max((cost_to_rob + rec(house_number + 2)), rec(house_number + 1))
            return self.dp[house_number]

        rec(0)
        return self.dp[0]
