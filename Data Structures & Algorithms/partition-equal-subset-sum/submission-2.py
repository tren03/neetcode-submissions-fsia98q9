class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}

        def rec(i,s1,s2):
            if i == len(nums) and s1 == s2:
                return True
            if i >= len(nums):
                return False
            if dp.get((i,s1,s2)) is not None:
                return dp[(i,s1,s2)]
            cur = nums[i]

            a = rec(i+1,s1+cur,s2)
            b = rec(i+1,s1,s2+cur)
            dp[(i,s1,s2)] = a or b
            return a or b

        return rec(0,0,0)

        