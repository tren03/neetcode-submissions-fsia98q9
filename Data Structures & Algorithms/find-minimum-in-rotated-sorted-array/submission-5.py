class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the sorted side, log the min val, eliminate that

        l,r = 0,len(nums)-1
        ans = nums[0]

        while(l<=r):
            m = (l+r)//2
            print(nums[m])

            # find the sorted side
            if nums[l] <= nums[m]:
                # left is sorted, so log min and remove left
                ans = min(ans,nums[l])
                l = m + 1
            else:
                # right is sorted, so log min and remove right
                ans = min(ans,nums[m])
                r = m - 1
        return ans




        
        