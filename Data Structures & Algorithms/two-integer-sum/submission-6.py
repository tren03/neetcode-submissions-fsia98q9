class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # val : index

        for ind,i in enumerate(nums):
            if target - i in m:
                t = m[target-i]
                return [t, ind]
            else:
                m[i] = ind

        