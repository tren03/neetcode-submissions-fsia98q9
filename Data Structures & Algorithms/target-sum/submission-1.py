class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}

        def rec(i , cur_sum):
            if i >= len(nums) and target == cur_sum:
                return 1
            if i >= len(nums):
                return 0
            if dp.get((i, cur_sum)) is not None:
                return dp[(i, cur_sum)]

            cur = nums[i]
            a = rec(i+1, cur_sum+cur)
            b = rec(i+1, cur_sum-cur)
            dp[(i,cur_sum)] = a+b
            return a+b
        return rec(0, 0)

        