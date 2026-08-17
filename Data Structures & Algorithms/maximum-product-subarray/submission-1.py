class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        ans = float('-inf') 

        for i in range(len(nums)):
            vp = nums[i]
            vs = nums[len(nums)-i-1]

            prefix *= vp 
            suffix *= vs

            ans = max([prefix,suffix,ans])

            if vp == 0:
                prefix = 1
            if vs == 0:
                suffix = 1

        return ans
            
            

                

        