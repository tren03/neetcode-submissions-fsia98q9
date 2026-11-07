class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        cur = 0
        while cur < len(nums):
            l = cur + 1
            r = len(nums) - 1

            while l < r and cur != l and cur != r:
                cur_sum = nums[cur] + nums[l] + nums[r]
                if cur_sum > 0:
                    # reduce r
                    while r-1 > l:
                        if nums[r-1] == nums[r]:
                            r -= 1
                            continue
                        else:
                            break
                    r -= 1
                else:
                    if cur_sum == 0:
                        ans.append([nums[cur], nums[l], nums[r]])
                    while l+1 < r:
                        if nums[l+1] == nums[l]:
                            l += 1
                            continue
                        else:
                            break
                    l += 1
            
            while cur+1 < len(nums):
                if nums[cur] == nums[cur+1]:
                    cur += 1
                    continue
                else:
                    break
            cur += 1
        return ans


            

