class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in nums: 
            if i in m:
                return True
            m[i]=True



                
        return False




         