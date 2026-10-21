class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        
        def rec(i, temp, cur):
            if i >= len(nums):
                return
            if cur > target:
                return 
            if cur == target:
                ans.append(temp.copy())
                return
            
            temp.append(nums[i])
            cur += nums[i]
            rec(i, temp, cur)
            cur-=nums[i]
            temp.pop()
            rec(i+1, temp, cur)
        rec(0,[],0)
        return ans
        