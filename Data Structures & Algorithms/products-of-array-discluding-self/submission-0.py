class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = [0]*len(nums)
        
        prod = 1 
        for index,nos in enumerate(nums):
            left[index]=prod
            prod *= nos
        
        
        prod = 1
        for index in range(len(nums)-1,-1,-1):
            right[index]=prod
            prod *= nums[index]
        
        ans = []
        print(left)
        print(right)
        for index,nos in enumerate(left):
            ans.append(nos*right[index])
        return ans
        
        
            