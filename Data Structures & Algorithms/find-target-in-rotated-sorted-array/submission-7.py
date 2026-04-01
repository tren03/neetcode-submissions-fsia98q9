class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check for sorted side
        # if target is within sorted side, remove unosorted side
        # else remove sorted side

        l = 0
        r = len(nums) -1

        while(l<=r):
            mid = (l+r)//2

            if target == nums[mid]:
                return mid

            # if left side sorted
            if nums[l] <= nums[mid]:
                # if target is within sorted side
                if target >= nums[l] and target <= nums[mid]:
                    # remove unsorted side
                    r = mid - 1
                else:
                    # since target is not in sorted range, remove sorted range
                    l = mid + 1
            else:
                # if target is within sorted side which is right now
                if target >= nums[mid] and target <= nums[r]:
                    # remove unsorted side
                    l = mid + 1
                else:
                    # since target is not in sorted range, remove sorted range
                    r = mid - 1
        return -1
                    

        