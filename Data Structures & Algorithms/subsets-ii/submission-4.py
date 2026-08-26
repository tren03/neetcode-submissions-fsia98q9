class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        def rec(i,arr):
            if i == len(nums):
                ans.append(arr.copy())
                return
            
            arr.append(nums[i])
            rec(i+1,arr)
            arr.pop()

            # skip dups
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            rec(i+1,arr)

        rec(0,[])
        return ans

        

        