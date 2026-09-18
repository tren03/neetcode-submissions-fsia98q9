class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur_min = cur_max = 1

        for i in range(len(nums)-1,-1,-1):
            cur = nums[i]
            a = cur * cur_min
            b = cur * cur_max
            cur_min = min(a,b,cur)
            cur_max = max(a,b,cur)
            ans = max(ans, cur_max)
        return ans
            


        