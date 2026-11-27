class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            mid = (l+r)//2
            mid_val = nums[mid]
            left_val = nums[l]
            right_val = nums[r]

            if mid_val == target:
                return mid

            # left half is sorted
            if left_val <= mid_val:
                if target >= left_val and target <= mid_val:
                    # remove r
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= mid_val and target <= right_val:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1










            

        