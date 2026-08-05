class Solution:
    def rob(self, nums: List[int]) -> int:
        # lets optimize this even more
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]


        a = nums[-1]
        b = max(nums[-2],nums[-1])
        for i in range(n-3,-1,-1):
            c = max(b, a+nums[i])
            a = b
            b = c
        return b




