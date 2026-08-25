class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        def rec(i, arr, cur):
            if i >= len(nums):
                return
            if cur > target:
                return
            if cur == target:
                ans.append(arr.copy())
                return

            arr.append(nums[i])
            rec(i,arr,cur+nums[i])
            arr.pop()

            rec(i+1,arr,cur)

        rec(0,[],0)
        return ans

            
        
        