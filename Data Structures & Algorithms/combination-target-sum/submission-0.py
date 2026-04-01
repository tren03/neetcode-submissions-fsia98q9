class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []

        def rec(temp,i,total):
            if total == target:
                ans.append(temp.copy())
                return
            if total > target:
                return
            if i == len(nums):
                return
            
            # same nos
            temp.append(nums[i])
            total += nums[i]
            rec(temp,i,total)

            # different nos
            temp.pop()
            total -= nums[i]
            rec(temp,i+1,total)
            
            
        rec(temp,0,0)
        return ans



        