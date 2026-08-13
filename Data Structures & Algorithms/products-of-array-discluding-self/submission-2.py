class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp = [1] * n
        rp = [1] * n
        ans = [1] * n

        running = 1
        for i in range(0,n):
            lp[i] = running
            running = running * nums[i]

        running = 1
        for i in range(n-1,-1,-1):
            rp[i] = running
            running = running * nums[i]
        

        for i in range(0,n):
            ans[i] = lp[i] * rp[i]
        return ans


        