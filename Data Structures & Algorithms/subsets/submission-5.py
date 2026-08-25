class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(i,arr):
            if i == len(nums):
                temp = arr.copy()
                ans.append(temp)
                return

            rec(i+1,arr)

            arr.append(nums[i])
            rec(i+1,arr)
            arr.pop()

        rec(0,[])
        return ans


        