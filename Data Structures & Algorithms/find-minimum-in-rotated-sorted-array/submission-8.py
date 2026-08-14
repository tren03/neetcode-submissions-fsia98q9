class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[0]
        
        while l <= r:
            m_index = (l+r)//2
            m_val = nums[m_index]

            # if nums[l] <= m_val <= nums[r]:
                #return nums[l]

            if nums[l] <= m_val:
                ans = min(ans, nums[l])
                l = m_index + 1
            else:
                ans = min(ans,m_val)
                r = m_index - 1

        return ans





        