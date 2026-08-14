class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid_index = (l + r) // 2
            mid = nums[mid_index]

            if target == mid:
                return mid_index
            
            if target < mid:
                r = mid_index - 1
            else:
                l = mid_index + 1
        return -1




