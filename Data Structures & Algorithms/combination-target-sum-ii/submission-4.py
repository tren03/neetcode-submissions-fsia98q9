class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        nums = candidates
        
        def rec(i, arr, cur):
            if cur == target:
                ans.append(arr.copy())
                return
            if i >= len(candidates):
                return
            if cur > target:
                return

            arr.append(nums[i])
            rec(i+1,arr,cur+nums[i])
            arr.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            rec(i+1,arr,cur)

            

        rec(0,[],0)
        return ans





            
        
        