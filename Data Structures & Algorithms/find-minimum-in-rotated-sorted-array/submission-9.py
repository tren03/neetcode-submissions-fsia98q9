class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ans = float('inf')

        while l <= r:
            mid = (l+r)//2
            mid_val = nums[mid]
            left_val = nums[l]
            right_val = nums[r]

            # left side is sorted
            if left_val <= mid_val:
                ans = min(ans, left_val)
                l = mid + 1
            else:
                ans = min(ans, mid_val)
                r = mid - 1
        
        return ans







            


        
        