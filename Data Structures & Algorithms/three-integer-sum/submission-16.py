class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums) 
        i = 0
        l = i + 1
        r = n - 1
        ans = []
        print(nums)

        while i < n:
            l = i + 1
            r = n - 1

            target = nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s < -target:
                    l += 1
                elif s > -target:
                    r -= 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    # skip dups here
                    l_val = nums[l]
                    r_val = nums[r]
                    l += 1
                    r -= 1
                    while l < r and l_val == nums[l]:
                        l += 1
                    while r > l and r_val == nums[r]:
                        r -= 1
                    continue
                
            i_val = nums[i]
            i += 1
            while i < n and i_val == nums[i]:
                i += 1
        return ans

                    








        