class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        r = 0
        cur_sum = 0

        while r < len(nums):
            if cur_sum < 0:
                cur_sum = nums[r]
                r += 1
                l = r
                ans = max(ans, cur_sum)
                continue

            if cur_sum >= 0:
                cur_sum += nums[r]
                ans = max(ans, cur_sum)
                r += 1
                continue


        return ans
        