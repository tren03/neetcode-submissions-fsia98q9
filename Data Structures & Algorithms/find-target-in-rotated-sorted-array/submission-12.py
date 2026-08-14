class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            m_index = (l+r)//2
            m_val = nums[m_index]

            if m_val == target:
                return m_index

            if nums[l] <= m_val:
                # left is sorted
                if nums[l] <= target and target <= m_val:
                    r = m_index - 1
                else:
                    l = m_index + 1
                continue
            
            if m_val <= nums[r]:
                # right is sorted
                if m_val <= target and target <= nums[r]:
                    l = m_index + 1
                else:
                    r = m_index - 1
                continue
            



                
        return ans


            

        